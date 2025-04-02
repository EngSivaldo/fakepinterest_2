from flask import render_template, url_for, flash, redirect
from fakepinterest import app
from fakepinterest.forms import FormLogin, FormCriarConta



#Links das telas----------------------------
#qualquer pessoa pode aceasar
@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/perfil/<usuario>')
#so acessa logado
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        flash(f'Login solicitado para {form.email.data}', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    form = FormCriarConta()
    if form.validate_on_submit():
        flash(f'Conta criada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('criar_conta.html', form=form)