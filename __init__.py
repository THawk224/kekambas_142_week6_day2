from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 

app = Flask(__name__)

# Configure the application
app.config.from_object(Config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing the models below
from .models import Task