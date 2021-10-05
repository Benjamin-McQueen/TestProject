from flask import Blueprint, render_template, request, json, jsonify, redirect, url_for
from sqlalchemy import delete

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
    username = User.query.get_or_404(request.json.get('data')).username
    email = User.query.get_or_404(request.json.get('data')).email
    id = User.query.get_or_404(request.json.get('data')).id
    # return redirect(url_for('route.user_manager'))
    return jsonify(username=username, email=email, id=id)


@routes.route("/deleteuserdata", methods=['POST'])
def delete_user_data():
    target = User.query.get_or_404(request.json.get('data'))

    if target == -1:
        return redirect(url_for('routes.user_manager'))

    database.session.delete(target)
    database.session.commit()

    return redirect(url_for('routes.user_manager'))


@routes.route("/edituserdata", methods=['POST'])
def edit_user_data():
    target = User.query.get_or_404(request.json.get('id'))
    if target == -1:
        return redirect(url_for('routes.user_manager'))

    target.username = request.json.get('username')
    target.email = request.json.get('email')

    new_pw = request.json.get('pw')
    if not new_pw == '':
        hashed_password = bcrypt.generate_password_hash(new_pw).decode('utf-8')
        target.pw = hashed_password

    database.session.commit()

    return redirect(url_for('routes.user_manager'))


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
    print('We got: ' + str(User.query.filter_by(username='CoolGuy').first()))
    return 'TODO'
