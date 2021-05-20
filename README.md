# Dockernized Django

This is barebone Django setup for docker & nginx & postgreserver all in one container.

## How to run

1. set private key

  cd www-cert
  
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client.key -out client.crt -config localhost.conf




2. Set environment variable

> export these value
  
~~~~
export APP_PORT=<Enter the port> 

export DJANGO_SQL_DATABASE=<SQL Database name> 

export DJANGO_SQL_USERNAME=<SQL Database username> 

export DJANGO_SQL_PASSWORD=<Password for the docker user> 

export DJANGO_DB_SECRET=<Enter DB Secret>

export DJANGO_DB_SERVICE_NAME=<Enter Service Name>

export DJANGO_DB_PORT=<Port for database>

export DJANGO_ADMIN_EMAIL=<Port for database>

export DJANGO_SUPERUSER_PASSWORD=<superuser password>

export DJANGO_SUPERUSER_EMAIL=<User Email>

export DJANGO_SUPERUSER_USERNAME=<Admin Username>
  
~~~~

> example 
  
~~~~

export APP_PORT=80

export DJANGO_SQL_DATABASE=django_db

export DJANGO_SQL_USERNAME=postgres


export DJANGO_SQL_PASSWORD=django_db_password

export DJANGO_DB_SECRET='5(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d'

export DJANGO_DB_SERVICE_NAME=db

export DJANGO_DB_PORT=5432

export DJANGO_SUPERUSER_PASSWORD=admin123

export DJANGO_SUPERUSER_EMAIL="admin@test.com"

export DJANGO_SUPERUSER_USERNAME=admin
  
~~~~



2. Compose Docker

docker-compose build

docker-compose up -d





3. Terminal
docker exec -it app /bin/sh