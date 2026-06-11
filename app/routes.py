from app import app
from flask import render_template, url_for, redirect 
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
        print("ta no caminho ")
        form.save()
        print("Dados salvos só q n kkkkkk")
    return render_template('competicoes.html', context=context , form=form) 

@app.route('/competicoes/financeiro', methods =['Get','POST'])
def competicoes_financeiro():

    dados = Competicoes.query.order_by('colocacao').all()
    
    print(dados)
    
    context = {}
    
    return render_template('competicoes_fin.html', context=context)

@app.route('/contratacoes',methods=['GET', 'POST'])
def contratacoes():
    return render_template('contratacoes.html')