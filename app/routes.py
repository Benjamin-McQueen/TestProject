from flask import Blueprint, render_template, request, json

from app.forms import CreateUser, FindUser, ModifyUser
from app.models import User
from app import database, bcrypt

routes = Blueprint('routes', __name__)

from app import CodeDebug


@routes.route("/")
@routes.route("/main")
def main_page():
    users = User.query.all()
    return render_template('mainpage.html', data=users)


@routes.route("/usermanagement", methods=['GET'])
def user_manager():
    users = User.query.all()
    user_form = ModifyUser()
    find_user_form = FindUser()
    return render_template('manageuser.html', users=users, fuform=find_user_form, userform=user_form)


@routes.route("/getuserdata", methods=['POST'])
def get_user_data():
    print(request.json)
    return 'TODO'


@routes.route("/newuser", methods=['GET', 'POST'])
def create_user():
    form = CreateUser()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.pw.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, pw=hashed_password)
        database.session.add(user)
        database.session.commit()
    return render_template('newuser.html', form=form)


@routes.route("/debugStuff")
def DEBUGGER_COMMAND():
    if CodeDebug:
        print("We're running with debug on.")
        user = User(username='Big Joe', email='BigJoe@Joe.Toe', pw='BadPassword')
        database.session.add(user)
        database.session.commit()
        return 'debug command fulfilled.'
    return 'not debugging.'
