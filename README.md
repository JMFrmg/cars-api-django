#API de gestion de garage avec Django

## Installation :
Se positionner dans le dossier principal de l'app

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


## Urls
Affichage de l'ensemble des cars:
http://127.0.0.1:8000/carsapi/car/

Formulaire de création d'une nouvelle car:
http://127.0.0.1:8000/carsapi/car/new

Affichage d'une car (remplacer <id> par l'id du car recherché)
http://127.0.0.1:8000/carsapi/car/<id>

