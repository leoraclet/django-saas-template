
backend: cd server && python manage.py runserver 0.0.0.0:8000
worker: cd server && celery -A config.celery worker --loglevel=info
beat: cd server && celery -A config.celery beat --loglevel=info
frontend: cd frontend && npm run dev
