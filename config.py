import yaml


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {'title': 'Fruit-Api', 'uiversion': 3}


class DevConfig(Config):
    props = yaml.load(open('./config/dev.yaml'), Loader=yaml.BaseLoader)
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        props['pg_user'], props['pg_pass'], props['pg_host'],
        props['pg_port'], props['pg_db'])


class TestConfig(Config):
    props = yaml.load(open('./config/test.yaml'), Loader=yaml.BaseLoader)
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        props['pg_user'], props['pg_pass'], props['pg_host'],
        props['pg_port'], props['pg_db'])
