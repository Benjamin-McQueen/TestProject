from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class ModifyUser(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    pw = StringField('Password')
    edit_button = SubmitField('Save User Data')
    delete_button = SubmitField('Delete User Data')


class FindUser(FlaskForm):
    username = SelectField('Select User')
    fubutton = SubmitField('Select This User')


class CreateUser(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    pw = PasswordField('Password', validators=[DataRequired()])
    cpw = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('pw')])
    submit = SubmitField('Confirm new User')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
