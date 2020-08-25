.PHONY: runserver makemigrations migrate
runserver:
	envdir envs/ python manage.py runserver

makemigrations:
	envdir envs/ python manage.py makemigrations

migrate:
	envdir envs/ python manage.py migrate

