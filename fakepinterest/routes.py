from flask import render_template, url_for, flash, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from fakepinterest.forms import FormLogin, FormCriarConta
from flask_login import login_required, login_user, logout_user, current_user

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def homepage():
    # Se o usuário já estiver autenticado, redireciona para o perfil
    if current_user.is_authenticated:
        return redirect(url_for('perfil', id_usuario=current_user.id))
    
    form_login = FormLogin()  # Cria uma instância do formulário de login
    if form_login.validate_on_submit():  # Verifica se o formulário foi preenchido corretamente
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()  # Busca o usuário pelo email
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):  # Verifica a senha
            login_user(usuario)  # Faz o login do usuário
            return redirect(url_for('perfil', id_usuario=usuario.id))  # Redireciona para o perfil do usuário
    return render_template('homepage.html', form=form_login)  # Renderiza a página inicial com o formulário de login

# Rota para criar uma nova conta
@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    form_criar_conta = FormCriarConta()  # Cria uma instância do formulário de criação de conta
    if form_criar_conta.validate_on_submit():  # Verifica se o formulário foi preenchido corretamente
        senha = bcrypt.generate_password_hash(form_criar_conta.senha.data)  # Criptografa a senha
        usuario = Usuario(username=form_criar_conta.username.data,
                          senha=senha,
                          email=form_criar_conta.email.data)  # Cria um novo usuário
        database.session.add(usuario)  # Adiciona o usuário ao banco de dados
        database.session.commit()  # Confirma a transação no banco de dados
        login_user(usuario, remember=True)  # Faz o login automático do usuário
        return redirect(url_for('perfil', id_usuario=usuario.id))  # Redireciona para o perfil do usuário
    return render_template('criar_conta.html', form=form_criar_conta)  # Renderiza a página de criação de conta com o formulário

# Rota para visualizar o perfil do usuário
@app.route('/perfil/<id_usuario>')
@login_required  # Exige que o usuário esteja logado para acessar esta rota
def perfil(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))  # Busca o usuário pelo ID
    if usuario:
        if int(id_usuario) == int(current_user.id):  # Verifica se o usuário está visualizando seu próprio perfil
            return render_template('perfil.html', usuario=current_user)  # Renderiza o perfil do usuário logado
        else:
            return render_template('perfil.html', usuario=usuario)  # Renderiza o perfil de outro usuário
    else:
        flash('Usuário não encontrado.', 'danger')  # Exibe uma mensagem de erro se o usuário não for encontrado
        return redirect(url_for('homepage'))  # Redireciona para a página inicial

# Rota para fazer logout
@app.route('/logout')
@login_required  # Exige que o usuário esteja logado para acessar esta rota
def logout():
    logout_user()  # Faz o logout do usuário
    flash('Você saiu da sua conta.', 'info')  # Exibe uma mensagem de confirmação de logout
    return redirect(url_for('homepage'))  # Redireciona para a página inicial