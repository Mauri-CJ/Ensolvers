from . import auth
from flask import render_template
from app.forms import LoginForm
from app.forms import SignupForm

@auth.route('/login')
def login():
    login=LoginForm()
    return render_template('login.html', form_login=login)

@auth.route('/signup')
def signup():
    signup = SignupForm()
    return render_template('signup.html',form_signup=signup)