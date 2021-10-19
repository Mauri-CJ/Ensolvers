from flask import Flask
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]="MY_SECRET_KEY"
    app.register_blueprint(auth)
    return app
