# HackathonSK

REST API для мобильного приложения, с помощью которого пользователи смогут отправлять информацию об объектах на сервер ФСТР.

Ссылка на сервис (REST API), где можно проверить, что он работает:
http://34.123.237.228:8000/

Документация:
http://34.123.237.228:8000/docs

Задача MVP1:
Отправка информации на сервер - код API(MVP1)
Пример запроса MVP1:
http://34.123.237.228:8000/docs#/default/add_to_added_submitData__post

Задача MVP2:
Пример запроса MVP2, получить одну запись (перевал) по её id:
http://34.123.237.228:8000/docs#/default/read_added_id_submitData__id___get

Пример запроса MVP2, получить статус модерации отправленных данных:
http://34.123.237.228:8000/docs#/default/read_added_id_submitData__id__status_get


Инструкция по публикации REST API на хостинг:
База данных в Google Cloud Platform,
Создана VM в Google Cloud Platform (Debian), установлены необходимые пакеты:
fastapi, sqlalchemy, psycopg2, uvicorn[standart]
