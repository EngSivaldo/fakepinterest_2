from flask import render_template, url_for, flash, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

# Página inicial => links
@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    
    nome_usuario = current_user.username if current_user.is_authenticated else None
    return render_template('homepage.html', form=formlogin, nome_usuario=nome_usuario)




# Criar conta
@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    form_criar_conta = FormCriarConta()
    if form_criar_conta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        #criar usuario /importar do models
        usuario = Usuario(username=form_criar_conta.username.data,
                          senha=senha,
                          email=form_criar_conta.email.data)
        #adiciona o usuario
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criar_conta.html', form=form_criar_conta)


# Perfil do usuário
@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    #verifica se usuario é o current_user
    if int(id_usuario) == int(current_user.id):
        #usuario ta vendo perfil dele
        form_foto = FormFoto()
        #criar funciolnalidade de enviar foto
        if form_foto.validate_on_submit():
            #pegar arquivo que esta dentro de compo foto
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)  # Garante nome seguro para o arquivo
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_seguro)
            arquivo.save(caminho)  # Salva o arquivo no diretório especificado
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form=form_foto)
    else:
        #caso contrario ta vendo perfil de outro usuario
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)


# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('homepage'))



@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()[:100]
    return render_template("feed.html", fotos=fotos)









# Nome Seguro para o Arquivo:

# nome_seguro = secure_filename(arquivo.filename): Garante que o nome do arquivo seja seguro para salvar no servidor.
# Caminho do Arquivo:

# caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_seguro): Cria o caminho completo onde o arquivo será salvo.
# Salvar o Arquivo:

# arquivo.save(caminho): Salva o arquivo no diretório especificado.
# Adicionar Foto ao Banco de Dados:

# foto = Foto(imagem=nome_seguro, id_usuario=current_user.id): Cria uma nova instância da foto com o nome seguro e o ID do usuário.
# database.session.add(foto): Adiciona a foto ao banco de dados.
# database.session.commit(): Confirma a transação no banco de dados.