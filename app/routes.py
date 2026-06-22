from app import app

from datetime import datetime, timedelta
from flask import render_template, url_for, redirect, request, flash

from app.form import *

@app.template_filter('milhar')
def milhar(valor):
    try:
        valor = float(valor)
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return "0,00"

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

@app.route('/gerar_folha', methods=['GET', 'POST'])
def gerar_folha():
    total_salario = 0
    jogadores = Jogador.query.all()
    for j in jogadores:
        total_salario += j.salario
    if total_salario == 0:
        flash("Nenhum salário cadastrado para os jogadores!", "warning")
        return redirect(url_for('financeiro'))
    nova_transacao = Transacao(
        tipo='DESPESA',
        valor_transacao=total_salario,
        descricao='Pagamento da Folha Salarial - Elenco',
        data_transacao=datetime.today()
    )
    try:
        db.session.add(nova_transacao)
        db.session.commit()
        flash(f"Folha de pagamento de R$ {total_salario:.2f} gerada e registrada no financeiro!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Erro ao registrar a folha no financeiro.", "danger")
        

    return redirect(url_for('financeiro_lista'))

@app.template_filter('dinheiro')
def formatar_dinheiro(valor):
    if valor is None:
        return "R$ 0.00"
    return f"R$ {valor:,.2f}".replace(',', '.')
    

@app.route('/financeiro', methods=['GET', 'POST'])
def financeiro():
    hoje = datetime.today()

    data_inicio_str = request.args.get('data_inicio')
    data_fim_str = request.args.get('data_fim')
    
    if data_inicio_str:
        data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d')
    else:
        data_inicio = hoje - timedelta(days=30)
        
    if data_fim_str:
        data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
    else:
        data_fim = hoje.replace(hour=23, minute=59, second=59)

    transacoes = Transacao.query.filter(
        Transacao.data_transacao >= data_inicio,
        Transacao.data_transacao <= data_fim
    ).all()

    total_receita = 0
    total_despesa = 0
    for transacao in transacoes:
        if transacao.tipo.upper() == 'RECEITA':
            total_receita += transacao.valor_transacao
        else:
            total_despesa += transacao.valor_transacao
            
    saldo_atual = total_receita - total_despesa
    
    context = {
        'transacoes': transacoes,
        'total_receita': total_receita,
        'total_despesa': total_despesa,
        'saldo_atual': saldo_atual,
        'data_inicio': data_inicio.strftime('%Y-%m-%d'),
        'data_fim': data_fim.strftime('%Y-%m-%d')
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


@app.route('/contratacoes',methods=['GET', 'POST'])
def contratacoes():
    form = TransferenciasForm() 

    context={}
    if form.validate_on_submit():
        form.save()
       
    return render_template('contratacoes.html', context=context , form=form)

@app.route('/contratacoes/historicos', methods=['GET', 'POST'])
def cont_historico():
    termo_pesquisa = request.args.get('pesquisa', '').strip()
    if termo_pesquisa:
        resultado = Transferencias.query.filter(Transferencias.nome.like(f"%{termo_pesquisa}%")).all()
    else:
        resultado = Transferencias.query.order_by(Transferencias.nome).all()
    context = {
        'dados': resultado
    }

    return render_template('transferencia.html', context=context)