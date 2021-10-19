from flask import render_template,redirect,url_for
from flask.helpers import flash
from app import create_app
from app.database import db
from flask_migrate import Migrate
from flask_login import login_required,LoginManager,current_user,logout_user
from app.models import Usuario,Carpeta,Tarea

USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='Ensolvers'
FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app= create_app()
app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter_by(id_usuario=user_id).first()

@app.route('/')
@login_required
def index():
    print(current_user.id_usuario)
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Nos vemos pronto!')
    return redirect(url_for('auth.login'))

