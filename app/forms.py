from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

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


class EditProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    about_me = TextAreaField('about', validators=[Length(min=0, max=512)])
    submit = SubmitField('submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('this username has been taken')


class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=1, max=140)])
    post = TextAreaField('post', validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField('submit')
