from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import config_options

from .main import main as main_blueprint
from .auth import auth as auth_blueprint

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # Initializing flask extensions
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    app.register_blueprint(orders_blueprint, url_prefix='/cart')

    return app
