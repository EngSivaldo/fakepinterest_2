from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nome usuário', validators=[DataRequired(), Length(min=2, max=20)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Criar Conta')
    
    def validate_email(self, email):
        from fakepinterest.models import Usuario
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")