# HackathonSK

REST API для мобильного приложения, с помощью которого пользователи смогут отправлять информацию об объектах на сервер ФСТР.

Ссылка на сервис (REST API), где можно проверить, что он работает:

Документация:
http://34.123.237.228:8000/docs

Задача MVP1:
Отправка информации на сервер - код API(MVP1): http://34.123.237.228:8000/docs#/default/add_to_added_submitData__post
Пример запроса MVP1: 
Request URL:http://34.123.237.228:8000/submitData/
Request body (JSON):
{
  "id": 12865,
  "beautyTitle": "пер.",
  "title": "Новый",
  "other_titles": "перевал2",
  "connect": "",
  "add_time": "2021-09-30 13:28:10",
  "user": {
    "id": "vpupkin",
    "email": "user@email.tld",
    "phone": 79031234567,
    "fam": "Пупкин",
    "name": "Василий",
    "otc": "Иванович"
  },
  "coords": {
    "latitude": "11.4565",
    "longitude": "7.5546",
    "height": "1315"
  },
  "type": "pass",
  "level": {
    "winter": "1А",
    "summer": "",
    "autumn": "2А",
    "spring": ""
  },
  "images": [
      {"url":"http://...", "title":"Подъём. Фото №1"},
      {"url":"http://...", "title":"Подъём. Фото №2"},
      {"url":"http://...", "title":"Седловина"},
      {"url":"http://...", "title":"Спуск. Фото №99"},
      {"url":"http://...", "title":"Спуск. Фото №99"}
  ]
}

Server response: "POST /submitData/ HTTP/1.1" 200 OK


Задача MVP2:
Пример запроса MVP2, получить одну запись (перевал) по её id:
http://34.123.237.228:8000/docs#/default/read_added_id_submitData__id___get
Пример запроса MVP2: 
Request URL:http://34.123.237.228:8000/submitData/2/
Parameters (id): 2
Server response: "GET /submitData/2/ HTTP/1.1" 200 OK


Пример запроса MVP2, получить статус модерации отправленных данных:
http://34.123.237.228:8000/docs#/default/read_added_id_submitData__id__status_get
Пример запроса MVP2: 
Request URL:http://34.123.237.228:8000/submitData/2/status
Parameters (id): 2
Server response: "GET /submitData/2/status HTTP/1.1" 200 OK
Response body: 
{
  "status": "new"
}


Инструкция по публикации REST API на хостинг:
База данных в Google Cloud Platform,
Создана VM в Google Cloud Platform (Debian), установлены необходимые пакеты:
fastapi, sqlalchemy, psycopg2, uvicorn[standart]
