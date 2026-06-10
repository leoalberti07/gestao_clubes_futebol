from app import app
from flask import render_template, url_for, redirect, request

from app.models import Jogador
from app.forms import JogadorForm

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/jogadores')
def jogadores():
    return render_template('jogadores.html')

@app.route('/financeiro', methods=['GET', 'POST'])
def financeiro():
    form = JogadorForm()
    form.posicao.choices = [
        ('GOL', 'Goleiro'),
        ('ZAG', 'Zagueiro'),
        ('MEI', 'Meio-Campo'),
        ('ATA', 'Atacante')
    ]
    
    form.status.choices = [
        ('ATIVO', 'Ativo'),
        ('LESIONADO', 'Lesionado'),
        ('EMPRESTADO', 'Emprestado'),
        ('INATIVO', 'Inativo')
    ]
    context = {}
    if form.validate_on_submit():
        form.save()
        print("dados salvos com sucesso")
        return redirect (url_for('homepage'))

    return render_template('financeiro.html', context=context, form=form)

@app.route('/financeiro_lista')
def financeiro_lista():
    lista_jogadores = Jogador.query.order_by(Jogador.nome).all()
    context = {
        jogadores: lista_jogadores
    }
    return render_template('financeiro_lista.html', context=context)

@app.route('/competicoes')
def competicoes():
    return render_template('competicoes.html')

@app.route('/contratacoes')
def contratacoes():
    return render_template('contratacoes.html')