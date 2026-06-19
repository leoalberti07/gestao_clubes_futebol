from flask import render_template, redirect, url_for
from app import app, db
from app.models import Jogador, Historico, competicoes
from app.form import JogadorForm

@app.route("/")
def homepage(): return render_template("index.html")

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Jogador
from app.form import JogadorForm

@app.route("/jogadores", methods=["GET", "POST"])
def jogadores():
    form = JogadorForm()
    if form.validate_on_submit():
        novo = Jogador(
            nome=form.nome_atleta.data,
            posicao=form.posicao_atleta.data,
            situacao=form.situacao_atleta.data,
            historico=form.historico_atleta.data
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('jogadores'))
    
    lista = Jogador.query.all()
    return render_template("jogadores.html", form=form, jogadores=lista)

@app.route("/historico", methods=["GET"])
def ver_historico():
    busca = request.args.get('busca')
    if busca:
        jogadores = Jogador.query.filter(Jogador.nome.contains(busca)).all()
    else:
        jogadores = Jogador.query.all()
    return render_template("historico.html", jogadores=jogadores)

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_jogador(id):
    jogador = Jogador.query.get_or_404(id)
    form = JogadorForm(obj=jogador) 
    
    if form.validate_on_submit():
        jogador.nome = form.nome_atleta.data
        jogador.posicao = form.posicao_atleta.data
        jogador.situacao = form.situacao_atleta.data
        jogador.historico = form.historico_atleta.data
        db.session.commit()
        return redirect(url_for('ver_historico')) 
        
    return render_template("editar.html", form=form, jogador=jogador)

@app.route("/financeiro")
def financeiro(): 
    return render_template("financeiro.html")

@app.route("/contratacoes")
def contratacoes(): 
    return render_template("contratacoes.html")

@app.route("/competicoes")
def competicoes(): 
    return render_template("competicoes.html")