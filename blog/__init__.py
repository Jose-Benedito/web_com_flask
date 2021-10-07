from flask import Flask
from flask.ctx import AppContext
from flask_sqlalchemy import SQLAlchemy # para o banco de dados
from flask_bcrypt import Bcrypt #para criptografar a senha

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meublog.db' #configurando o nome do Bd
app.config['SECRET KEY'] = 'dscergthyyyjew987'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from blog.admin import route