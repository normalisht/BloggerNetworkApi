# BloggerNetworkAPI

### Описание
Проект социальная сети которая позволяет публиковать посты и оставлять под ними
комментарии. Так же можно подписываться на интересных авторов и группы.
У каждого поста есть список тем к которым он относится и для каждой темы
есть отдельная группа, в которой находятся связанные посты.

### Стек
* Django Rest Framework
* SQLite
* Git
* Postman

### Как запустить проект
* Клонировать репозиторий:
```bash
git clone git@github.com:normalisht/BloggerNetworkApi.git
```

* Создать и активировать виртуальную среду, установить зависимости
```bash
python -m venv venv
if [ -e "venv/bin/activate" ]; then
    source venv/bin/activate
else
    source venv/Scripts/activate
fi
pip install -r requirements.txt
```

* Перейти в папку проекта:

```bash
cd yatube_api
```

* Выполнить миграции:

```bash
python manage.py migrate
```

* Создать администратора:

```bash
python manage.py createsuperuser
```

* Запустить проект:

```bash
python3 manage.py runserver
```

### Документация находится в файле `yatube_api/static/redoc.yaml`

### Примеры запросов к API

#### Получение публикаций с 11 по 20 (GET):

```/api/v1/posts/?offset=10&limit=10```

Формат ответа:

```JSON
{
  "count": 12,
  "next": null,
  "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=10",
  "results": [
    {
      "id": 11,
      "author": "norman",
      "text": "Some text",
      "pub_date": "2023-04-03T12:05:16.012992Z",
      "image": null,
      "group": null
    },
    {
      "id": 12,
      "author": "norman",
      "text": "Some text",
      "pub_date": "2023-04-03T12:05:16.639890Z",
      "image": null,
      "group": null
    }
  ]
}
```

#### Запрос для создания публикации (POST):

```/api/v1/posts/```

Тело запроса:
```JSON
{ "text": "Some text" }
```
Формат ответа:

```JSON
{
  "id": 1,
  "author": "norman",
  "text": "Some text",
  "pub_date": "2023-04-03T12:02:24.017693Z",
  "image": null,
  "group": null
}
```

#### Подписаться на пользователя (POST):
```/api/v1/follow/```

Тело запроса:
```JSON
{ "following": "username" }
```

Формат ответа:
```JSON
{ 
  "user": "your_username",  
  "following": "username"
}
```
