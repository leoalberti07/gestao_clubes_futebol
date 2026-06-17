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
    termo_pesquisa = request.args.get('pesquisa', '').strip()
    if termo_pesquisa:
        resultado = Competicoes.query.filter(Competicoes.competicao.like(f"%{termo_pesquisa}%")).all()
    else:
        resultado = Competicoes.query.order_by(Competicoes.colocacao).all()
    context = {
        'dados': resultado
    }
    return render_template('competicoes_fin.html', context=context)

@app.route('/contratacoes',methods=['GET', 'POST'])
def contratacoes():
    return render_template('contratacoes.html')
