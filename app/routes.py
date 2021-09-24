from flask import Blueprint, render_template

from app.models import User

routes = Blueprint('routes', __name__)


@routes.route("/")
@routes.route("/main")
def main_page():
    users = User.query.all()
    return render_template('mainpage.html', data=users)


@routes.route("/newuser")
def new_user():
    return 'TODO'


@routes.route("/usermanagement")
def user_manager():
    return 'TODO'
