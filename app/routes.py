from app import app
from flask import render_template, url_for, redirect

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/jogadores')
def jogadores():
    return render_template('jogadores.html')

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

@app.route('/competicoes')
def competicoes():
    return render_template('competicoes.html')

@app.route('/contratacoes')
def contratacoes():
    return render_template('contratacoes.html')