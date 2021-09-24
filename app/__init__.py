import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

import app
from app.config import Config

database = SQLAlchemy()
bcrypt = Bcrypt()
CodeDebug = True

if CodeDebug:
    from app.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import routes
    app.register_blueprint(routes)

    database.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        database.create_all()

    return app
