import yaml

props = yaml.load(open('db.yaml'), Loader=yaml.BaseLoader)
psqlUrl = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(props['pg_user'], props['pg_pass'], props['pg_host'], props['pg_port'], props['pg_db'])
SQLALCHEMY_DATABASE_URI = psqlUrl
SQLALCHEMY_TRACK_MODIFICATIONS = False