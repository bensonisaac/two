
# HNGx Person API

REST API capable of CRUD operations


## Installation
Run the app locally

Clone the repository
```  
git clone https://github.com/bensonisaac/two.git
```
Create a virtual environment 
```
python -m venv .venv && .venv/Scripts/activate
```
Cd into the project folder
```
cd two
```
Install the project dependencies
```
pip install -r requirements.txt
```
Open the settings.py file and turn DEBUG to False

Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
Test
```
python manage.py test api
```
Run the dev server
```
python manage.py runserver
```
## Documentation

[Documentation](https://github.com/bensonisaac/two/blob/main/DOCUMENTATION.md)


## Tech Stack

**Server:** Python/Django, djangorestframework
**Database:** PostgreSQL 

