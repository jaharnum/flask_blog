'''
view functions
'''
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'crash'},
            'body': 'Max is sleeping on my arm right now'
        },
        {
            'author': {'username' : 'crash'},
            'body': 'Gimme sympathy by Metric is playing'
        },
    ]
    return render_template(
            'index.html', posts=posts) 


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('Invalid username')
            return redirect(url_for('login'))
        
        if not user.check_password(password=form.password.data):
            flash('Invalid password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        # if netloc isn't this app its suspicious to redirect there after login
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            
        return redirect(next_page)

    return render_template('login.html', title='crashtestblog - login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()

    if form.validate_on_submit():

        # create the User
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        # add the new user to the database
        db.session.add(user)
        db.session.commit()

        flash('successfully registered')
        return redirect(url_for('login'))

    return render_template('register.html', title='register', form=form)
