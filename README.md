# fruit-app

<p align="center">
  <img width="200" src="flask-logo.png" alt="FastApi logo">
  <p align="center">
    Flask + SQLAlchemy + PostgreSQL REST API to store fruits
  </p>
</p>

# Get started

## Unix

Install pipenv:

```bash
sudo apt install python3-venv
pip3 install pipenv
```

Then create the folder for allocate the virtual environment:

```bash
mkdir .venv
```

Launch pipenv:

```bash
pipenv install
```

Then activate the virtual env:

```bash
pipenv shell
```

Run command inside virtualenv:

```bash
pipenv run
```

Exit virtual env:

```bash
exit or deactivate
```

## Windows

Update pip:

```bash
py -m pip install --upgrade pip
```

Install python3-venv:

```bash
py -m pip install virtualenv
```

Then create the folder for allocate the virtual environment:

```bash
py -m virtualenv env
```

Then activate the virtual env:

```bash
Set-ExecutionPolicy Unrestricted -Scope Process (run if UnauthorizedAccess in powershell console)
.\venv\Scripts\activate.ps1
```

Now you can install python libs as you need it

Check our current installed packages:

```bash
py -m pip list
```

De-activate virtual env:

```bash
deactivate
```

# set up

Configure all your dependencies in Pipfile.
See: https://pypi.org/

# api-ref

See under dev_tools folder the insomnia file with related endpoints
See also flasgger implementation on {api_host}:{api_port}/apidocs

# sqlalchemy

For init db:

```bash
flask db init
flask db migrate
flask db update
```

re-create db:

```bash
flask db upgrade
```

# launch

## Unix

```bash
python3 app.py
```

or

```bash
flask run
```

## Windows

```bash
py app.py
```

or

```bash
flask run
```

# usefull ref

- https://docs.sqlalchemy.org/en/13/orm/query.html
- https://flask-marshmallow.readthedocs.io/en/latest/
- https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/
- https://blog.mphomphego.co.za/blog/2018/09/14/How-I-configured-SonarQube-for-Python-code-analysis.html
