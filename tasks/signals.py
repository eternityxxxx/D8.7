from django.db.models.signals import m2m_changed, post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import TodoItem, Category, Priorities
from collections import Counter


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action != 'post_add':
        return

    for cat in instance.category.all():
        slug = cat.slug

        new_count = 0
        for task in TodoItem.objects.all():
            new_count += task.category.filter(slug=slug).count()

        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action != "post_remove":
        return

    cat_counter = Counter()
    for t in TodoItem.objects.all():
        for cat in t.category.all():
            cat_counter[cat.slug] += 1

    for slug, new_count in cat_counter.items():
        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(pre_save, sender=TodoItem)
def todo_preadd(sender, instance, **kwargs):
    priority, created = Priorities.objects.get_or_create(name=instance.priority)

    if instance.priority:
        priority, created = Priorities.objects.get_or_create(name=instance.priority)

    if created:
        Priorities.objects.filter(name=priority.name).update(count=1)
        return

    new_count = priority.count + 1
    Priorities.objects.filter(name=priority.name).update(count=new_count)
    return


@receiver(post_save, sender=TodoItem)
def todo_postadd(sender, instance, **kwargs):
    priority, created = Priorities.objects.get_or_create(name=instance.priority)

    if created:
        Priorities.objects.filter(name=priority.name).update(count=1)
        return

    new_count = priority.count + 1
    Priorities.objects.filter(name=priority.name).update(count=new_count)
    return


@receiver(post_delete, sender=TodoItem)
def todo_delete(sender, instance, **kwargs):
    priority, created = Priorities.objects.get_or_create(name=instance.priority)

    if created:
        Priorities.objects.filter(name=priority.name).update(count=0)
        return

    new_count = priority.count - 1
    Priorities.objects.filter(name=priority.name).update(count=new_count)
    return
