# fruit-app

# Get started
Install python3-venv:
sudo apt install python3-venv
Then create the folder for allocate the virtual environment:
python3 -m venv venv
The activate the virtual env:
source venv/bin/activate
Install flask:
pip3 install flask

Code in {% %} is called Jinja - See Jinja templata engine

# set up
For generate requirements.txt file please execute:
pip3 freeze > requirements.txt

Having requirements.txt a quick way to install dependencies is:
pip3 install -r requirements.txt

# sqlalchemy
For init db
flask init db
flask db migrate
flask db update

# launch
python3 app.py

# usefull ref
* https://docs.sqlalchemy.org/en/13/orm/query.html
* https://flask-marshmallow.readthedocs.io/en/latest/
* https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/
* https://flask.palletsprojects.com/en/1.1.x/errorhandling/
* https://www.askpython.com/python-modules/flask/flask-crud-application
* https://medium.com/bitproject/recently-i-created-a-restful-api-with-flask-where-my-models-had-many-parameters-75da1db870b7