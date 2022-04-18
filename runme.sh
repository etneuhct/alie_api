python manage.py migrate
gunicorn alie_api.wsgi:application -p 8000 & nginx -g "daemon off;"