# API YaMDb
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-ff9900?style=flat&logo=django&logoColor=white)
![Postman](https://img.shields.io/badge/-Postman-FF6C37?style=flat&logo=postman&logoColor=white)
## Описание проекта
Данный проект основан на моделях машинного обучения для выявления подозрительных транзакций. Инструкции указаны ниже.

## Ресурсы RinHack
- auth: аутентификация.
- users: пользователи.
- titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- reviews: отзывы на произведения.
- comments: комментарии к отзывам.


## Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/iNTENSY/RinHack.git
```
```
```
- Cоздать и активировать виртуальное окружение
```
python3 -m venv venv # Для Linux и macOS
python -m venv venv # Для Windows
```
```
venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Перейти в папку со скриптом управления и выполнить миграции
```
cd backend
```
```
python manage.py migrate
```

- Запустить проект
```
python manage.py runserver
```
## Полная документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API. Перед этим запустить сервер командой,
приведенной выше

```
http://127.0.0.1:8000/redoc/
```
## Над проектом работали
