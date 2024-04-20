
# Инструкция

## Технологии
Python 3.12
Django 5.0
## Клонирование проекта
```
git clone https://github.com/TheSweetieTea/tree-menu.git
```
## Создание виртуального окружения
```
python3 -m venv venv 
```
## Активация виртуального окружения
```
source venv/bin/activate
```
## Скопируйте и настройте значения переменных окружения
```
cp .env.example .env
```
## Установка зависимостей
```
pip3 install -r requirements.txt
``` 
## Миграции
- Создание миграциий
```
python3 manage.py makemigrations
```
- Применение миграции
```
python3 manage.py migrate
```
## Создание супер пользователя
```
python3 manage.py createsuperuser
```
## Запуск проекта в dev-режиме
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
## Тестирование проекта
- Перейдите в папку c manage.py и выполните команду:
```
python3 manage.py test
```
