from app import app
from flask import render_template

@app.route('/')
def index():
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