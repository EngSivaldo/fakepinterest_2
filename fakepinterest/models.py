from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
  return Usuario.query.get(int(id_usuario))

# Tabelas--------------------
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), nullable=False, unique=True)
    senha = database.Column(database.String(80), nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.username}>'

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(200), default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return f'<Foto {self.imagem}>'
