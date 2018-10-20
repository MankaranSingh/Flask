import sys, os
sys.path.insert(0, os.path.abspath('..'))
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):         #Application Factory

    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    
    bootstrap.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager.init_app(app)

    from .main import error, main
    
    app.register_blueprint(error)
    app.register_blueprint(main)

    return app
    
