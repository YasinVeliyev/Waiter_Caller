from flask import Flask
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
login_manager = LoginManager(app)


from waitercaller import routes