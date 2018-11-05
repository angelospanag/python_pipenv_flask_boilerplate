import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

# Extensions
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    print(config_name + " configuration loaded", file=sys.stderr)

    # Initialise app configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialise extensions
    # SQLAlchemy
    db.init_app(app)

    # Module Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
