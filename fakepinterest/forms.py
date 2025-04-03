from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from fakepinterest.models import Usuario

# Formulário de login
class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Campo de email com validação
    senha = PasswordField('Senha', validators=[DataRequired()])  # Campo de senha com validação
    botao_confirmacao = SubmitField('Fazer Login')  # Botão de confirmação

# Formulário de criação de conta
class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Campo de email com validação
    username = StringField('Nome usuário', validators=[DataRequired(), Length(min=2, max=20)])  # Nome de usuário com validação de comprimento
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])  # Senha com validação de comprimento
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])  # Confirmação de senha
    submit = SubmitField('Criar Conta')  # Botão de criação de conta
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()  # Verifica se o email já está cadastrado
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")  # Lança erro se o email já estiver cadastrado

# Formulário de upload de foto
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])  # Campo de upload de foto com validação
    botao_confirmacao = SubmitField('Enviar')  # Botão de confirmação
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     Validação de Email:

# def validate_email(self, email): Método para verificar se o email já está cadastrado no banco de dados.
# usuario = Usuario.query.filter_by(email=email.data).first(): Consulta o banco de dados para verificar se o email já existe.
# raise ValidationError("E-mail já cadastrado, faça login para continuar"): Lança um erro de validação se o email já estiver cadastrado.
# Campos de Formulário:

# email = StringField('Email', validators=[DataRequired(), Email()]): Campo de email com validação para garantir que o valor é obrigatório e um email válido.
# senha = PasswordField('Senha', validators=[DataRequired()]): Campo de senha com validação para garantir que o valor é obrigatório.
# confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')]): Campo de confirmação de senha com validação para garantir que corresponde à senha.