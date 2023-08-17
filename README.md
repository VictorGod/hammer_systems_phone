## API для авторизации и управления профилями пользователей
 # Установка
В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости: python3 -m venv venv . venv/bin/activate pip install -r requirements.txt

Выполните миграции:

python manage.py migrate

Запустите сервер: python manage.py runserver

Ваш проект запустился на http://127.0.0.1:8000/

# Запрос на ввод номера телефона
URL: http://127.0.0.1:8000/api/auth/profile/
Метод: POST
Параметры запроса:
Параметр:	phone_number,    
Тип: string,	    	
Описание: Номер телефона;
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
# Запрос на ввод кода авторизации
URL: http://127.0.0.1:8000/api/auth/authorize/
Метод: POST
Параметр:	phone_number  ,  
Тип: string,   	
Описание: Номер телефона,
Параметр:	authorization_code;   
Тип: string,	    	
Описание:  Код авторизации;

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


  {
    "message": "Авторизация успешна"
  }
```
Ошибка:
```json
  {
    "message": "Неверный код авторизации"
  }
```

# Профиль пользователя
Запрос на получение профиля пользователя
URL: http://127.0.0.1:8000/api/auth/profile/
Метод: POST
Параметры запроса:
Параметр:	phone_number,    
Тип: string,	    	
Описание: Номер телефона;
Параметр:	invite_code,   
Тип: string,	    	
Описание:  Инвайт-код;

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
# Активация инвайт-кода
URL: http://127.0.0.1:8000/api/auth/profile/
Метод: POST
Параметры запроса:
Параметр:	phone_number,    
Тип: string,	    	
Описание: Номер телефона;
Параметр:	invite_code,   
Тип: string,	    	
Описание:  Инвайт-код;
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
# Список пользователей, введших инвайт-код
Запрос на получение списка пользователей
URL: http://127.0.0.1:8000/api/auth/invited_users/
Метод: GET
Параметры запроса:
Параметр:	phone_number    
Тип: string,	    	
Описание: Номер телефона;
Пример запроса:
http://127.0.0.1:8000/api/auth/invited_users?phone_number=89065310821
Ответ:
Успешный ответ:
```json
  {
    "invited_users": [
      "0987654321"
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
