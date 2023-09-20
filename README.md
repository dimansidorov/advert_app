# Advert App

Небольшое приложение на django и django_rest_framework

Models:

- Category - категории объявлений, поля: name 
- City - город объявления, поля: name 
- Advert - объявление, поля: title, description, city, category, views

Views:

- /api/advert-list/ - json список объявлений со всеми полями 
- /api/advert/<pk>/ - json detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении


## Стек
- Python 3.11
- Django 4.2.5
- djangorestframework 3.14.0
- Postgres 16.0

## Инструкция по запуску проекта:

- `docker-compose build` - сборка проекта
- `docker-compose up` - запуск проекта
- `docker-compose run --rm advert-app sh -c "python manage.py createsuperuser"` - создание суперпользователя

## Лицензия

MIT