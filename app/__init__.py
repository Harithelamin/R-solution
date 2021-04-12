from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
template_folder = "./app/templates/"
app.config['SECRET_KEY'] = 'ldsmkjgcdgvdsjmg@#%^*&^*&^lkjflkgjlkfdjgjdglkfdjgldkjglk^%$^%$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///R-solution.db'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
db.create_all()
