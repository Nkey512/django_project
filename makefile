deploy:
	export DJANGO_SETTINGS_MODULE=hello_django.settings && \
	gunicorn hello_django.wsgi
