## API для авторизации и управления профилями пользователей
# Запрос на ввод номера телефона
URL: /profile
Метод: POST
Параметры запроса:
Toggle word wrap: off
Download as CSV
Параметр	Тип	Описание
phone_number	string	Номер телефона
Пример запроса:
```json

{
  "phone_number": "1234567890"
}
```
Ответ:
Успешный ответ:
```json
  {
    "phone_number": "1234567890",
    "authorization_code": "1234",
    "invite_code": "ABC123",
    "activated_invite_code": null
  }
```
Ошибка:
```json
  {
    "message": "Пользователь не найден"
  }
```
Запрос на ввод кода авторизации
URL: /authorize
Метод: POST

Параметр	             Тип	        Описание
phone_number	         string	      Номер телефона
authorization_code	   string	      Код авторизации
Пример запроса:
```json
{
  "phone_number": "1234567890",
  "authorization_code": "1234"
}
```
Ответ:
Успешный ответ:
```json

Copy

  {
    "message": "Авторизация успешна"
  }
```
Ошибка:
```json
  {
    "message": "Неверный код авторизации"
  }

Профиль пользователя
Запрос на получение профиля пользователя
URL: /profile
Метод: POST
Параметры запроса:
Параметр	    Тип	    Описание
phone_number	string	Номер телефона
invite_code	  string	Инвайт-код
Пример запроса:
```json
{
  "phone_number": "1234567890",
  "invite_code": "ABC123"
}
```
Ответ:
```json
{
  "phone_number": "1234567890",
  "authorization_code": "1234",
  "invite_code": "ABC123",
  "activated_invite_code": null
}
```
Активация инвайт-кода
URL: /profile
Метод: POST
Параметры запроса:
Параметр	    Тип	    Описание
phone_number	string	Номер телефона
invite_code	  string	Инвайт-код
Пример запроса:
```json



{
  "phone_number": "1234567890",
  "invite_code": "ABC123"
}
```
Ответ:
```json
{
  "phone_number": "1234567890",
  "authorization_code": "1234",
  "invite_code": "ABC123",
  "activated_invite_code": "ABC123"
}
```
Список пользователей, введших инвайт-код
Запрос на получение списка пользователей
URL: /invited_users
Метод: GET
Параметры запроса:

Параметр	    Тип	    Описание
phone_number	string	Номер телефона
Пример запроса:
/invited_users?phone_number=1234567890
Ответ:
Успешный ответ:
```json
  {
    "invited_users": [
        0987654321
      "9876543210"
    ]
  }
```
Ошибка:
```json
  {
    "message": "Пользователь не найден"
  }
```

Данное API позволяет пользователям авторизоваться по номеру телефона, получить свой профиль, активировать инвайт-код и получить список пользователей, которые ввели инвайт-код текущего пользователя.
Postman коллекцию со всеми запросами можно найти по ссылке.
