# Веб-приложение для просмотра погоды
## Сделано:
* Тесты
* Помещено в докер-контейнер
* API для просмотра истории поиска и количества введенных городов

## Используемые технологии:
* Python
* Django Framework и Django Rest Framework
* Docker
* Git
* API https://open-meteo.com/ 
* Bootstrap

## Тестирование (Docker)
### 1. Клонировать репозиторий:
```git clone ...```
### 2. Перейти в директорию:
```cd weather_app```
### 3. Добавить файл .env (c вводом ключа django):
```echo SECRET_KEY="YOUR_DJANGO_KEY" > .env```
### 4. Запустить Docker Desktop
### 5. Собрать образ и запустить контейнер:
```docker-compose up```

## API документация:
* */api* — Корень API
* */api/users* — Смотреть пользователей
* */api/history* — Смотреть историю просмотра пользователя
* */api/cities* — Смотреть информацию по городам
* */api-token-auth* — Получить токен аутентификации