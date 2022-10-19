from flask import Flask, render_template, request, session, redirect
from config import app_config, app_active
import sys
from importlib import reload

from config import app_config, app_active
config = app_config[app_active]

def create_app():
    app = Flask(__name__)
    
    user = {
        'marlon':{
        'nome': 'marlon',
        'senha': '1234',
        'caminho': 'https://covid-19-dash-asimov.herokuapp.com/'},
        'nathan':{
        'nome': 'nathan',
        'senha': '1234',
        'caminho': 'https://real-estate-dash.herokuapp.com/'},
        'marcelo':{
        'nome': 'marcelo',
        'senha': '1234',
        'caminho': 'https://sales-analyzer-app-dash.herokuapp.com/'}
    }
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cadastro')
    def cadastro():
        return "Em construção"


    @app.route('/login', methods=["GET", "POST"])
    def login():

        usuario = ""
        erro = ""
        senha = ""
        if request.method == "POST":

            usuario = request.form['usuario']
            senha = request.form['senha']

            if usuario == "" or senha == "":

                erro = "Preencha todos os campos"

                return render_template('login.html',erro=erro, usuario=usuario)

            if usuario in user:

                if senha != user[usuario]['senha']:

                    erro = "Senha incorreta"

                    return render_template('login.html',erro=erro, usuario=usuario)

                else:

                    nome= usuario

                    id = user[usuario]['nome']
                    caminho = user[usuario]['caminho']

                    return redirect(f'/usuario/{id}')

            else:

                erro = "Usuário incorreto"

                usuario = request.form['usuario']

                return render_template('login.html',erro=erro, usuario=usuario)

        elif request.method == "GET":

            return render_template('login.html', usuario=usuario)

    @app.route('/usuario/<string:id>', methods=["GET", "POST"])
    def usuario(id):

        return render_template('usuario.html', id=user[id]['nome'], nome=user[id]['nome'],caminho=user[id]['caminho'])


    return app



app = create_app(app_active)

if __name__ == '__main__':
    app.run()