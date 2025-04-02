from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from fakepinterest import Usuario

#formulários 
class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nome usuário', validators=[DataRequired(), Length(min=2, max=20)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha =  PasswordField('Senha', validators=[DataRequired(), EqualTo("senha")])
    submit = SubmitField('Criar Conta')
    
    
    def validate_email(self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
        return ValidationError("E-mail ja cadastrado, faça login para continuar")
          
    