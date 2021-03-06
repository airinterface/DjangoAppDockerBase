#!/bin/sh


echo "$PWD"

echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"



# Wait for few minute and run db migraiton
#while ! python manage.py makemigrations  2>&1; do
#   echo "Migration is in progress status"
#   sleep 3
#done

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput



if [[ ! -z "${DJANGO_SUPERUSER_USERNAME}" ]] && [[ ! -z "${DJANGO_SUPERUSER_EMAIL}" ]];
then
  echo "Creating admin user $DJANGO_SUPERUSER_USERNAME ..."
  python manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME"\
       --email "${DJANGO_SUPERUSER_EMAIL}" 2> /dev/null || \
    echo "Superuser ${DJANGO_SUPERUSER_USERNAME} already exists"
else
  echo "Environment variable not set ${DJANGO_SUPERUSER_USERNAME},${DJANGO_SUPERUSER_EMAIL}"
fi




echo "Django docker is fully configured successfully."

echo "Starting Gunicorn."
exec python manage.py runserver 0.0.0.0:8000


exec "$@"
