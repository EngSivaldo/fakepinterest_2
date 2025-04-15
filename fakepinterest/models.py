from fakepinterest import database, login_manager
from flask_login import UserMixin #CLASSE QUE GERENCIA LOGIN
from datetime import datetime


#funcao que carrega um usuario
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


# Modelo de usuário (TABELAS)
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)  # ID único do usuário
    username = database.Column(database.String(80), nullable=False)  # Nome de usuário
    email = database.Column(database.String(120), nullable=False, unique=True)  # Email único
    senha = database.Column(database.String(80), nullable=False)  # Senha criptografada
    fotos = database.relationship('Foto', backref='usuario', lazy=True)  # Relacionamento com fotos

    def __repr__(self):
        return f'<Usuario {self.username}>'

# Modelo de foto
class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)  # ID único da foto
    imagem = database.Column(database.String(200), default='default.png')  # Caminho da imagem
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)  # Data de criação
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)  # ID do usuário

    def __repr__(self):
        return f'<Foto {self.imagem}>'
    
    
    
    
    
    
    
    
    
    
    
    
    
#     Relacionamento com Fotos:

# fotos = database.relationship('Foto', backref='usuario', lazy=True): Define um relacionamento entre o usuário e suas fotos. backref='usuario' cria uma referência inversa, permitindo acessar o usuário a partir de uma foto.
# Caminho da Imagem:

# imagem = database.Column(database.String(200), default='default.png'): Define o caminho da imagem com um valor padrão.
# Data de Criação:

# data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow): Define a data de criação da foto com o valor padrão sendo a data e hora atual.
# Chave Estrangeira:

# id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False): Define uma chave estrangeira que referencia o ID do usuário.