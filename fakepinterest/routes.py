#Rotas(links)
from flask import render_template, url_for
#import o app se nao funciona(do __init__.py)
from fakepinterest import app
#restringe acesso a pagina
from flask_login import login_required



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



