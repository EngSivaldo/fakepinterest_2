from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Criar a aplicação
app = Flask(__name__)

# Configurar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercadinho.db'
app.config['SECRET_KEY'] = "b96e7276ab4c35d03c19a252baf153a4"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

# Importar as rotas (precisa do routes para funcionar)
from fakepinterest import routes