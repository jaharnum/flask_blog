from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

''' WHEN CHANGING DB MODELS:
    - make changes here as needed
    - WHEN CHANGES ARE COMPLETE run:
       flask db migrate
       (optional) flask db migrate -m "model names separated by spaces"
    - this will generate a .py file in the migrations\versions folder
    - double check this file to ensure it reflects your changes
    - then you can run
        flask db upgrade
    - this will update the internal sqlite database
    - commit the .py file and use flask db upgrade on other devices as needed
    - you can also run flask db downgrade if you need to reverse it
'''

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):

    '''
    UserMixin handles: is_authenticated, is_active, is_anonymous, and get_id()

    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64))  # TODO, NOT IMPLEMENTED

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    about_me = db.Column(db.String(512))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))  # TODO, NOT IMPLEMENTED
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)