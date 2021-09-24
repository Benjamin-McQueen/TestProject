from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

import app
from app.config import Config

database = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import routes
    app.register_blueprint(routes)

    database.init_app(app)
    bcrypt.init_app(app)

    database.create_engine()
    database.create_all()

    return app
