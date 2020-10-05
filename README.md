# D8.7
## Module D8 homework

### Данные от админки:
```
    Логин: pws_admin
    Пароль: sf_password
```

### Страница с кешем:
```
    /time
```

#### Как развернуть проект:
1. Создаем новый каталог виртуального окружения:
```
    python -m venv <Имя каталога>
```
2. Стянуть репозиторий к себе:
```
    git clone https://github.com/eternityxxxx/D8.7.git
```
3. Активируем виртуальное окружения:
```
    <Имя каталога>/Scripts/activate
```
4. Установить зависимости из requirements.txt:
```
    pip install -r requirements.txt
```
5. Произвести миграции:
```
    cd 'pws-django-todoapp-heroku'
    python manage.py makemigrations
    python manage.py migrate
```
6. Запускаем сервер:
```
    python manage.py runserver
```