# TestovoePythonDev

Проект развернут по IP: [103.45.247.177](http://103.45.247.177)

## Swagger документация

Swagger доступен по ссылке: `api/v1/swagger`

## Сброс пароля

Функция сброса пароля (`reset_password`) отправляет уведомления в консоль. Для отправки на почту используется настройка `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`.

## Парсер

Парсер находится в файле `link/utils.py`. Не подключался Celery, так как это не было предусмотрено в ТЗ.

## Настройка окружения

Для запуска проекта необходимо создать файл `.env` со следующими полями:

DJANGO_SECRET_KEY = ""
POSTGRES_DB = ""
POSTGRES_USER = ""
POSTGRES_PASSWORD = ""
POSTGRES_HOST = ""
POSTGRES_PORT = ""
POSTGRES_ENGINE = ''
ALLOWED_HOSTS = ''
USER_AGENT = ""

Затем выполните команду `docker-compose up -d`.

# основные url для пользователя
    регистрация : /auth/users/ (post запрос)
    смена пароля : /auth/users/set_password/
    сброс пароля : /auth/users/reset_password/
    аутентификация : /auth/jwt/create (refresh : /auth/jwt/refresh)
остальное смотреть в swagger
## SQL скрипт

Для получения статистики ссылок можно использовать следующий SQL-запрос:

```sql
SELECT  
    u.email, 
    COUNT(l.id) AS count_links,
    SUM(CASE WHEN l.link_type = 'website' THEN 1 ELSE 0 END) AS website,
    SUM(CASE WHEN l.link_type = 'book' THEN 1 ELSE 0 END) AS book,
    SUM(CASE WHEN l.link_type = 'article' THEN 1 ELSE 0 END) AS article,
    SUM(CASE WHEN l.link_type = 'music' THEN 1 ELSE 0 END) AS music,
    SUM(CASE WHEN l.link_type = 'video' THEN 1 ELSE 0 END) AS video
FROM 
    user_user u
LEFT JOIN 
    link_link l ON u.id = l.user_id
GROUP BY 
    u.id, u.email
ORDER BY 
    count_links DESC, u.id ASC
LIMIT 
    10;
Тестовые данные были сгенерированы с использованием faker