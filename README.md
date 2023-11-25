# Единоразово:

python -m venv venv

venv/Scripts/activate

pip install -r .\requirements.txt

cd backend

py manage.py migrate


# Для запуска сервера
py manage.py runserver