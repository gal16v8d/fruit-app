from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
#from flask_wtf.csrf import CSRFProtect
from api.doc.swagger import swagger
from api.schema.root_schema import ma
from api.model.database import db
from api.route.fruit_route import api


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    #csrf = CSRFProtect()
    # csrf.init_app(app)
    Bootstrap(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)
    app.register_blueprint(api, url_prefix='/api')
    return app


if __name__ == '__main__':
    main_app = create_app()
    main_app.run()
