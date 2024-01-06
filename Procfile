web: gunicorn lecabinetdemacassar.wsgi --log-file -
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn lecabinetdemacassar.wsgi:application