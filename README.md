# HackathonSK

REST API для мобильного приложения, с помощью которого пользователи смогут отправлять информацию об объектах на сервер ФСТР.


Задача MVP1:
Отправка информации на сервер - код API(MVP1): 
Request URL: POST/submitData/

Request body (JSON)

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
