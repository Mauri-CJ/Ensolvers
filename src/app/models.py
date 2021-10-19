from .database import db
from flask_login import UserMixin

class Usuario(UserMixin,db.Model):
    id_usuario = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    contraseña = db.Column(db.String(250))
    carpetas = db.relationship('Carpeta',backref="usuario")

    def get_id(self):
           return (self.id_usuario)

class Carpeta(db.Model):
    id_carpeta = db.Column(db.Integer,primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),nullable=False)
    nombre = db.Column(db.String(50))
    tareas = db.relationship('Tarea',backref="Carpeta")

class Tarea(db.Model):
    id_tarea = db.Column(db.Integer,primary_key=True)
    id_carpeta = db.Column(db.Integer, db.ForeignKey('carpeta.id_carpeta'),nullable=False)
    nombre = db.Column(db.String(50))
    estado = db.Column(db.Boolean())

