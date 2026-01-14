import flask
from flask import Flask, render_template
import random # necessário para utilizar o módulo random

app = Flask(__name__)
# Toda pagina tem
# Router/Rota -> Caminho depois da URL(dominio)  localnews.com/cadastro.py
# Função -> O que vc quer mostrar na pagina.
# Templetes -> Sera a pasta onde ficara todas as paginas HTML do nosso Site.
# @ Decoretor - Atribui uma funcionalidade a um comando/funcao neste caso exibira a função na pagina.
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/conexao")
def conexao():
    return render_template("conexao.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

# Primeira Pagina

# Segunda Pagina

#Colocando pagina no ar

if __name__ == "__main__":
    app.run(debug=True)
