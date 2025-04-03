from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercadinho.db'  # Configura o banco de dados
app.config['SECRET_KEY'] = "b96e7276ab4c35d03c19a252baf153a4"  # Chave secreta para segurança
app.config['UPLOAD_FOLDER'] = "static/fotos_posts"  # Diretório para salvar imagens

database = SQLAlchemy(app)  # Inicializa SQLAlchemy
bcrypt = Bcrypt(app)  # Inicializa Bcrypt para criptografia
login_manager = LoginManager(app)  # Inicializa LoginManager
login_manager.login_view = 'homepage'  # Define a rota de login

@login_manager.user_loader
def load_user(user_id):
    from fakepinterest.models import Usuario  # Importa o modelo de usuário
    return Usuario.query.get(int(user_id))  # Carrega o usuário pelo ID

from fakepinterest import routes  # Importa as rotas









# Configurações do Flask:

# app.config['SQLALCHEMY_DATABASE_URI']: Define o URI do banco de dados SQLite.
# app.config['SECRET_KEY']: Define uma chave secreta para segurança da aplicação.
# app.config['UPLOAD_FOLDER']: Define o diretório onde as imagens serão salvas.
# Inicialização de Extensões:

# database = SQLAlchemy(app): Inicializa SQLAlchemy para manipulação do banco de dados.
# bcrypt = Bcrypt(app): Inicializa Bcrypt para criptografia de senhas.
# login_manager = LoginManager(app): Inicializa LoginManager para gerenciamento de sessões de usuário.
# Carregamento de Usuário:

# @login_manager.user_loader: Decorador que define a função para carregar o usuário pelo ID.
# return Usuario.query.get(int(user_id)): Carrega o usuário do banco de dados pelo ID.
# Importação de Rotas:

# from fakepinterest import routes: Importa as rotas da aplicação.