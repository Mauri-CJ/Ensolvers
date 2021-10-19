from . import auth

@auth.route('/login')
def login():
    return "Login"

@auth.route('/signup')
def signup():
    return "Signup"