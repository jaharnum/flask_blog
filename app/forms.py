from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

from app.models import User


class LoginForm(FlaskForm):

    # validators are all methods bc they need to perform actions
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('log in')


class RegistrationForm(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', 
                validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('retype your password', 
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # validate_<field_name> methods are used as custom validators
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('username has been taken')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('email has been registered to another account')
