from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField,BooleanField
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

class AgregarCarpetaForm(FlaskForm):
    nueva_carpeta= StringField("Agregar Carpeta", validators = [DataRequired()])
    crear =  SubmitField("Agregar")

class AgregarTareaForm(FlaskForm):
    nueva_tarea= StringField("Agregar Tarea", validators = [DataRequired()])
    estado = BooleanField("¿Hecho?")
    crear =  SubmitField("Agregar")

class EditarTareaForm(FlaskForm):
    editar_tarea= StringField("Editar Tarea", validators = [DataRequired()])
    estado = BooleanField("¿Hecho?")
    crear =  SubmitField("Editar")





