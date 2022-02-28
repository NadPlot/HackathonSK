# HackathonSK

REST API для мобильного приложения, с помощью которого пользователи смогут отправлять информацию об объектах на сервер ФСТР.
Задача MVP1:
Отправка информации на сервер - код API(MVP1)
Пример запроса:

curl -X 'POST' \
  'http://127.0.0.1:8000/submitData/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 12685,
  "beautyTitle": "пер.",
  "title": "Новый",
  "other_titles": "Тест",
  "connect": "",
  "add_time": "2021-09-25 13:18:13",
  "user": {
    "id": "vpupkin",
    "email": "mail@mail.ru",
    "phone": 123456789,
    "fam": "pupkin",
    "name": "vasya",
    "otc": "ivanovich"
  },
  "coords": {
    "latitude": "14.256",
    "longitude": "12.654",
    "height": "1300"
  },
  "type": "pass",
  "level": {
    "winter": "",
    "summer": "1А",
    "autumn": "",
    "spring": "2А"
  },
  "images": {
    "images": [{"url":"http://...", "title":"Подъём. Фото №1"}, {"url":"http://...", "title":"Подъём. Фото №2"}, {"url":"http://...", "title":"Седловина"}, {"url":"http://...", "title":"Спуск. Фото №99"}, {"url":"http://...", "title":"Спуск. Фото №99"}]
  }
}'



Ссылка на сервис (REST API), где можно проверить, что он работает:


Инструкция по деплою на хостинг - как развернуть приложение:


Примеры запросов для API. Использование Swagger — будет преимуществом.
