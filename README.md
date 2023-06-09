# Создание и обработка заказов

## Описание
Система позволяе регестривроватся пользователям как заказчик и как исполнитель.
Заказчик может регистрироваться, создавать заказы, просматривать свои заказы.
Исполнитель может регистрироваться, смотреть все заказы и менять статус заказов
на Исполнено и Отклонено. Исполнителю доступна статистика.

### Технологии
- Python 3.9
- Django 3.2

### Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него:
```
git clont git@github.com:lllleeenna/orders_test.git
```
```
cd orders_test
```
Создайте и активируйте виртуальное окружение:
```
python3.9 -m venv venv
```
```
source venv/bin/activate
```
Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Перейдите в папку orders_test, выполните миграции и запустите проект:
```
cd orders_test
```
```
python manage.py migrate
```
```
python manage.py runserver
```
### Автор
Смурова Елена (https://github.com/lllleeenna)