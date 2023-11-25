# RinHack
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-ff9900?style=flat&logo=django&logoColor=white)
![Postman](https://img.shields.io/badge/-Postman-FF6C37?style=flat&logo=postman&logoColor=white)
## Описание проекта
Данный проект основан на моделях машинного обучения для выявления подозрительных транзакций. Инструкции указаны ниже.


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
1) http://127.0.0.1:8000/schema/download/ Ссылка на скачивание YAML файла с инструкциями
2) http://127.0.0.1:8000/swagger ссылка на swagger
3) http://127.0.0.1:8000/redoc ссылка на автоматически созданную документацию
```
## Над проектом работали
Головинский Семён, Даценко Дмитрий, Геннадий Погуляй, Симоненков Николай, Воробьёв Максим
