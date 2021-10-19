from typing import ValuesView
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email_usuario =  StringField("Email",validators=[DataRequired()])
    contraseña = PasswordField("Contraseña",validators=[DataRequired()])
    enviar = SubmitField("Ingresar")

class SignupForm(FlaskForm):
    nombre_usuario = StringField("Nombre",validators=[DataRequired()])
    email_usuario =  StringField("Email",validators=[DataRequired()])
    contraseña = PasswordField("Contraseña",validators=[DataRequired()])
    enviar = SubmitField("Registrarse")

class AgregarForm(FlaskForm):
    nueva_carpeta= StringField("Agregar Carpeta", validators = [DataRequired()])
    crear =  SubmitField("Agregar")