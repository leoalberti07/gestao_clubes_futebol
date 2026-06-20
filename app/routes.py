from app import app

from flask import render_template, url_for, redirect,request

from app.form import *

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route('/jogadores', methods=['GET', 'POST'])
def jogadores():
    form = JogadorForm()
    lista = Jogador.query.all()

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('jogadores'))
    
    return render_template("jogadores.html", form=form, jogadores=lista)


@app.route('/financeiro', methods=['GET', 'POST'])
def financeiro():
    transacoes = Transacao.query.all()
    total_receita = 0
    total_despesa = 0
    for transacao in transacoes:
        if transacao.tipo == 'RECEITA':
            total_receita += transacao.valor_transacao
        else:
            total_despesa += transacao.valor_transacao
    saldo_atual = total_receita - total_despesa
    context ={
        'total_receita': total_receita,
        'total_despesa': total_despesa,
        'saldo_atual': saldo_atual
    }
    return render_template('financeiro.html', context=context)

@app.route('/financeiro_transacoes', methods=['GET', 'POST'])
def financeiro_transacoes():
    form = TransacaoForm()
    form.tipo.choices = [
        ('RECEITA', 'receita'),
        ('DESPESA', 'despesa')
    ]
    
    form.descricao.choices = [
        ("PATROCINIO MASTER", "Patrocínio master"),
        ("PATROCINIOS SECUNDARIOS", "Patrocínios Secundários"),
        ("SOCIO-TORCEDOR","Sócio-Torcedor"),
        ("BILHETERIA", "Bilheteria (Ingressos)"),
        ("PRODUTOS LICENCIADOS", "Venda de Produtos Licenciados"),
        ("DIREITOS DE TRANSMISSAO", "Cotas de TV e Direitos de Transmissão"),
        ("PREMIACAO", "Premiações de Campeonatos"),
        ("VENDA/TRANSFERENCIA", "Venda / Transferência de Atletas"),
        ("ALUGUEL ESTADIO", "Aluguel do Estádio / Eventos"),
        #despesas
        ("SALARIO JOGADORES", "Salário do Elenco (Jogadores)"),
        ("SALARIO STAFF", "Salário da Comissão Técnica e Staff"),
        ("MANUTENCAO ESTADIO", "Manutenção do Estádio e Gramado"),
        ("VIAGENS HOSPEDAGEM", "Despesas com Viagens e Hospedagem"),
        ("COMPRA ATLETAS", "Contratação / Compra de Novos Atletas"),
        ("TAXAS FEDERACAO", "Impostos e Taxas da Federação"),
        ("LOGISTICA EQUIPAMENTOS", "Logística e Equipamentos (Material Esportivo)"),
        ("CONTAS GERAIS", "Contas Gerais (Água, Luz, Internet do CT)"),
        ("INVESTIMENTO BASE", "Investimento nas Categorias de Base")
    ]
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect (url_for('financeiro'))

    return render_template('financeiro_transacoes.html', context=context, form=form)

@app.route('/financeiro_lista')
def financeiro_lista():
    termo_pesquisa = request.args.get('pesquisa', '').strip()
    if termo_pesquisa:
        resultado = Transacao.query.filter(Transacao.descricao.like(f"%{termo_pesquisa}%")).all()
    else:
        resultado = Transacao.query.order_by(Transacao.id.desc()).all()
    context = {
        'transacoes': resultado
    }

    return render_template('financeiro_lista.html', context=context)

@app.route('/financeiro/excluir/<int:id>', methods=['POST'])
def excluir_transacao(id):
    transacao = Transacao.query.get_or_404(id)
    try:
        db.session.delete(transacao)
        db.session.commit()
        print(f"Transação {id} excluída com sucesso!")
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao excluir transação: {e}")
    return redirect(url_for('financeiro_lista'))

@app.route('/competicoes', methods=['GET', 'POST'])
def competicoes():
    form = CompeticoesForm() 

    context={}
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
        jogador.salario = form.salario.data
        db.session.commit()
        return redirect(url_for('ver_historico')) 
        
    return render_template("editar.html", form=form, jogador=jogador)
