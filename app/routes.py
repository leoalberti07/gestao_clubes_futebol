from app import app
from flask import render_template, url_for, redirect,request
from app.form import CompeticoesForm
from app.models import Competicoes


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route('/jogadores', methods=['GET', 'POST'])
def jogadores():
    return render_template('jogadores.html')

@app.route('/financeiro',methods=['GET', 'POST'])
def financeiro():
    return render_template('financeiro.html')

@app.route('/competicoes', methods=['GET', 'POST'])
def competicoes():
    form = CompeticoesForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('competicoes')) 
    return render_template('competicoes.html', context=context , form=form)

@app.route('/competicoes/financeiro', methods =['GET','POST'])
def competicoes_financeiro():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Competicoes.query.order_by('colocacao')
    if pesquisa != '':
        dados = dados.filter_by(competicoes=pesquisa)
    context = {'dados': dados.all()}
    
    return render_template('competicoes_fin.html', context=context)

@app.route('/contratacoes',methods=['GET', 'POST'])
def contratacoes():
    return render_template('contratacoes.html')