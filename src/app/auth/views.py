from flask import request,flash,render_template
from flask.helpers import url_for
from werkzeug.utils import redirect
from . import auth
from flask_login import login_user,current_user
from app.forms import LoginForm
from app.forms import SignupForm
from app.models import Usuario
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login=LoginForm()
    if  request.method  == 'POST':
        if login.validate_on_submit():
            email_form = login.email_usuario.data
            usuario_db = Usuario.query.filter_by(email=email_form).first()
            if usuario_db != None:
                contraseña_form =  login.contraseña.data
                if check_password_hash(usuario_db.contraseña,contraseña_form):
                    login_user(usuario_db)
                    flash("Bienvenido de nuevo")
                    return redirect(url_for('index'))
                else:
                    flash("El usuario y/o contraseña no coinciden!")
            else:
                flash("El usuario y/o contraseña no coinciden!")
            
            

    return render_template('login.html', form_login=login)

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signup = SignupForm()
    if request.method == 'POST':
        if signup.validate_on_submit():
            email_form = signup.email_usuario.data
            usuario_db = Usuario.query.filter_by(email=email_form).first()
            if usuario_db != None:
                flash('El email no está disponible')
            else:
                nombre_form = signup.nombre_usuario.data
                contraseña_form= generate_password_hash(signup.contraseña.data)
                usuario_nuevo = Usuario(nombre=nombre_form,email=email_form,contraseña=contraseña_form)
                db.session.add(usuario_nuevo)
                db.session.commit()
                login_user(usuario_nuevo)
                flash("Bienvenido!")
                return redirect(url_for('index'))

    return render_template('signup.html',form_signup=signup)