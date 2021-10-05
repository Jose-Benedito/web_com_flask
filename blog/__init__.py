from flask import Flask
from flask.ctx import AppContext
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meublog.db'
db = SQLAlchemy(app)

from blog.admin import route