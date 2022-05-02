# HackathonSK

REST API для мобильного приложения, с помощью которого пользователи смогут отправлять информацию об объектах на сервер ФСТР.


Задача MVP1:
Отправка информации на сервер - код API(MVP1): 
Request URL: POST/submitData/
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
GET /submitData/:id — получить одну запись (перевал) по её id
Server response: "GET /submitData/2/ HTTP/1.1" 200 OK

Задача MVP2_2:
GET /submitData/:id/status — получить статус модерации отправленных данных.
Request URL:GET/submitData/2/status
Server response: "GET /submitData/2/status HTTP/1.1" 200 OK
Response body: 
{
  "status": "new"
}



В ходе решения поставленной задачи, было выполено:
1. Развернут dump базы данных (на локальном компьютере (а затем на хостинге), PostgreSQL). Использован Google Cloud Platform.
2. Создана VM в Google Cloud Platform (Debian), установлены необходимые пакеты: fastapi, sqlalchemy, psycopg2, uvicorn[standart]. 
