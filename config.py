import yaml
from dotenv import dotenv_values


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {'title': 'Fruit-Api', 'uiversion': 3}


class DevConfig(Config):
    config = dotenv_values('.env')
    SQLALCHEMY_DATABASE_URI = config['DB_URL']


class TestConfig(Config):
    config = dotenv_values('.env.test')
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = config['DB_URL']
