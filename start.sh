#!/bin/bash

# Roda as migrações
python manage.py makemigrations
python manage.py migrate

# Inicia o servidor
python manage.py runserver 0.0.0.0:$PORT
