'''
view functions
'''
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Post

'''
@login_required - user will be redirected to login screen if not logged in
'''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('post added successfully')
        return redirect(url_for('index'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template(
            'index.html', form=form, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        # we are already logged in, return to homepage
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('This username does not exist')
            return redirect(url_for('login'))

        if not user.check_password(password=form.password.data):
            flash('This password is incorrect')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        # if netloc isn't this app its suspicious to redirect there after login
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        # 'next_page' could be any view with @login_required
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

@app.route('/<username>')
@login_required
def user(username):
    # raises a 404 for you if user is not found
    user = User.query.filter_by(username=username).first_or_404()
    # gets user's posts in chronological order
    posts = user.get_posts()
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('your changes have been saved')
        return redirect(url_for('edit_profile'))

    elif request.method == 'GET':
        # load the current username and about
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='edit profile', form=form)
