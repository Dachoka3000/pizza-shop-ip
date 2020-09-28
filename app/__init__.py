from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config_options

<<<<<<< HEAD
=======

>>>>>>> 3793f106813b15ef6db6705bc2a6fa300afffe91

bootstrap = Bootstrap()
db = SQLAlchemy()
mail=Mail()


def create_app(config_name):
    app = Flask(__name__)

    # Initializing flask extensions
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .menus import orders as orders_blueprint

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint


    # Registering blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(orders_blueprint, url_prefix='/cart')

    return app
