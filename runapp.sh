#! /bin/bash
mkdir ./data/logs/

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn core.wsgi:application -b 0.0.0.0:8000 --reload --log-level='debug' --log-file=./data/logs/gunicorn.log --access-logfile=./data/logs/gunicorn-access.log --error-logfile=./data/logs/gunicorn-error.log
