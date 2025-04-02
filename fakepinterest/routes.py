from flask import render_template, url_for, flash, redirect
from fakepinterest import app
from fakepinterest.forms import FormLogin, FormCriarConta
from flask_login import login_required

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()
    return render_template('homepage.html', form=form_login)

@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    form_criar_conta = FormCriarConta()
    if form_criar_conta.validate_on_submit():
        flash(f'Conta criada para {form_criar_conta.username.data}!', 'success')
        return redirect(url_for('homepage'))
    return render_template('criar_conta.html', form=form_criar_conta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)