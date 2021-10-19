from app import create_app
from app.database import db
from flask_migrate import Migrate
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

@app.route('/')
def index():
    return "Welcome to my page"

