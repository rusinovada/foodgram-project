# Проект foodgram-project-react

![Yamdb Workflow Status](https://github.com/rusinovada/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)

## Описание проекта

«Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Проект в интернете

Проект запущен и доступен по [адресу](http://178.154.231.253/recipes/)

## Шаблон наполнения .env

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с
postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД

## Команды для запуска приложения в контейнерах

В директории с файлом docker-compose выполнить команду в терминале

```bash
docker-compose up -d --build 
```

Выполните миграции

```bash
docker-compose exec backend python manage.py migrate
```

Создайте суперпользователя

```bash
docker-compose exec backend python manage.py createsuperuser
```

Соберите статику

```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

Чтобы остановить контейнеры, выполните в терминале команду

```bash
docker-compose down -v 
```

## Команды для заполнения бд

Для заполнения бд необходимо зайти на (<http://localhost/admin/>), войти в профиль суперюзера и внести необходимые данные. Для создания резервной копии бд выполните команду

```bash
docker-compose exec backend python manage.py dumpdata > fixtures.json
```

### Разработчики

* [Дарья Русинова](https://github.com/rusinovada)
* Верный друг - Круассан
