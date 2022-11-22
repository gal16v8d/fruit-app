# fruit-app

# Get started

## Unix

Install pipenv:
pip3 install pipenv
Then create the folder for allocate the virtual environment:
mkdir .venv
Launch pipenv:
pipenv install --skip-lock
Then activate the virtual env:
pipenv shell
Run command inside virtualenv:
pipenv run
Exit virtual env:
exit or deactivate

## Windows

Update pip:
py -m pip install --upgrade pip
Install python3-venv:
py -m pip install virtualenv
Then create the folder for allocate the virtual environment:
py -m virtualenv env
Then activate the virtual env:
Set-ExecutionPolicy Unrestricted -Scope Process (run if UnauthorizedAccess in powershell console)
.\venv\Scripts\activate.ps1
Now you can install python libs as you need it

Check our current installed packages:
py -m pip list
De-activate virtual env:
deactivate

# set up

Configure all your dependencies in Pipfile.
See: https://pypi.org/

# api-ref

See under dev_tools folder the insomnia file with related endpoints
See also flasgger implementation on {api_host}:{api_port}/apidocs

# sqlalchemy

For init db:
flask db init
flask db migrate
flask db update

re-create db:
flask db upgrade

# launch

## Unix

python3 app.py or flask run

## Windows

py app.py or flask run

# usefull ref

- https://docs.sqlalchemy.org/en/13/orm/query.html
- https://flask-marshmallow.readthedocs.io/en/latest/
- https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/
- https://blog.mphomphego.co.za/blog/2018/09/14/How-I-configured-SonarQube-for-Python-code-analysis.html
