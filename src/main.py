from flask import render_template,redirect,url_for,request
from flask.helpers import flash
from jinja2.utils import contextfunction
from app import create_app
from app.database import db
from app.forms import AgregarCarpetaForm, AgregarTareaForm,EditarTareaForm
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

@app.route('/',methods = ['GET','POST'])
@login_required
def index():
    id_usuario = current_user.id_usuario
    nombre_usuario = current_user.nombre
    carpetas = Carpeta.query.filter_by(id_usuario=id_usuario)
    agregar_form = AgregarCarpetaForm()
    context = {
        'id_usuario':id_usuario,
        'nombre_usuario': nombre_usuario,
        'carpetas':carpetas,
        'agregar_form' : agregar_form,
    }

    if request.method == 'POST':
        if agregar_form.validate_on_submit():
            carpeta = Carpeta(id_usuario=current_user.id_usuario,nombre=agregar_form.nueva_carpeta.data)
            db.session.add(carpeta)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('index.html',**context)

@app.route('/ver/<int:id>/<string:nombre>',methods=['GET','POST'])
def ver_tareas(id,nombre):
    tareas=Tarea.query.filter_by(id_carpeta=id)
    agregar_form = AgregarTareaForm()
    context = {
        'nombre_carpeta' : nombre,
        'id_carpeta':id,
        'tareas' : tareas,
        'agregar_tarea' : agregar_form
    }

    if request.method == 'POST':
        if agregar_form.validate_on_submit():
            tarea = Tarea(id_carpeta=id,nombre=agregar_form.nueva_tarea.data,estado=agregar_form.estado.data)
            db.session.add(tarea)
            db.session.commit()
            return redirect(url_for('ver_tareas',id=id,nombre=nombre))

    return render_template('ver_tareas.html',**context)

@app.route('/eliminar_carpeta/<int:id>')
def eliminar_carpeta(id):
    carpeta =  Carpeta.query.filter_by(id_carpeta=id).first()
    tareas =  Tarea.query.filter_by(id_carpeta=id)
    for tarea in tareas:
        db.session.delete(tarea)
    db.session.delete(carpeta)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/eliminar_tarea/<int:id>/')
def eliminar_tarea(id):
    tarea =  Tarea.query.filter_by(id_tarea=id).first()
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar_tarea/<int:id>', methods=['GET','POST'])
def editar_tarea(id):
    editar_form= EditarTareaForm()
    tarea =  Tarea.query.filter_by(id_tarea=id).first()
    context = {
        'editar_form' : editar_form,
        'tarea':tarea
    }
    if request.method == 'POST':
        tarea =  Tarea.query.filter_by(id_tarea=id).first()
        nombre = request.form['nombre']
        estado = request.form.get('hecho')
        if estado == 'on':
            hecho=True
        else:
            hecho=False

        tarea.nombre=nombre
        tarea.estado=hecho
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar.html',**context)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Nos vemos pronto!')
    return redirect(url_for('auth.login'))

