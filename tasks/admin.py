from django.contrib import admin
from .models import TodoItem, Category, Priorities


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')


@admin.register(Priorities)
class PrioritiesAdmin(admin.ModelAdmin):
    pass
