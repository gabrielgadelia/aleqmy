from flask import Flask, app
from flask_login import *

from .configs import Config
from .extensions import db, migrate
from app.user.views import user_bp



def create_app():
    app = Flask(__name__)
    # set configs
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_filters(app)
    return app



def loginmanager():
    login_manager = LoginManager()
    login_manager.init_app(app)

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_filters(app):
    pass


def register_blueprints(app):
    bps = [user_bp]
    for bp in bps:
        app.register_blueprint(bp)