pip install -r requirements.txt

gunicorn --bind 127.0.0.1:5000 wsgi:app