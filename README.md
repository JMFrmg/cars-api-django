#API de gestion de garage avec Django

## Installation :
Se positionner dans le dossier principal de l'app

pip install -r requirements.txt</br>
python manage.py makemigrations</br>
python manage.py migrate</br>
python manage.py runserver</br>


## Urls
Affichage de l'ensemble des cars:</br>
http://127.0.0.1:8000/carsapi/car/

Formulaire de création d'une nouvelle car:</br>
http://127.0.0.1:8000/carsapi/car/new

Affichage d'une car (remplacer <id> par l'id du car recherché):</br>
http://127.0.0.1:8000/carsapi/car/<id>

