#!/bin/sh
echo "Starting ..."

cd ..

echo ">> Deleting old migrations"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# Optional
echo ">> Deleting database"
find . -name '*sqlite3' -delete

echo ">> Running manage.py makemigrations"
python manage.py makemigrations 
python manage.py makemigrations appTest1

echo ">> Running manage.py migrate"
python manage.py migrate
python manage.py migrate --database=test1

echo ">> Done"

