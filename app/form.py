from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from app.models import *
from app import db


class JogadorForm(FlaskForm):

    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0, max=70)])
    posicao = SelectField('posição', validators=[DataRequired()], choices=[
        ('GOL', 'Goleiro'),
        ('ZAG', 'Zagueiro'),
        ('LAT', 'Lateral'),
        ('MEI', 'Meio-Campo'),
        ('ATA', 'Atacante')
    ])
    numero_camisa = IntegerField('Numero da camisa', validators=[DataRequired(), NumberRange(min=1, max=99)])
    status = SelectField('Status', validators=[DataRequired()], choices=[
        ('ATIVO', 'Ativo / No Elenco'),
        ('LESIONADO', 'Lesionado'),
        ('EMPRESTADO', 'Emprestado'),
        ('RESERVA', 'Reserva')
    ])
    valor_mercado = FloatField('Valor de mercado', validators=[DataRequired(), NumberRange(min=0, max=100000000000)])
    salario = FloatField('Salário', validators=[DataRequired(), NumberRange(min=1621, max=100000000)])
    btn_submit = SubmitField('Enviar')

    def save(self):

        jogador = Jogador(
            nome = self.nome.data,
            idade = self.idade.data,
            posicao = self.posicao.data,
            numero_camisa = self.numero_camisa.data,
            status = self.status.data,
            valor_mercado = self.valor_mercado.data,
            salario = self.salario.data
        )

        db.session.add(jogador)
        db.session.commit()

class TransacaoForm(FlaskForm):
    tipo = SelectField('Tipo de transação', validators=[DataRequired()], choices=[
        ('RECEITA', 'receita'),
        ('DESPESA', 'despesa')
    ])
    valor_transacao = FloatField('Valor da transação', validators=[DataRequired(), NumberRange(min=0.01)])
    descricao = SelectField('Descrição da transação', validators=[DataRequired()], choices=[
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
    ])

    def save(self):

        transacao = Transacao(
            tipo = self.tipo.data,
            valor_transacao = self.valor_transacao.data,
            descricao = self.descricao.data,
            
        )

        db.session.add(transacao)
        db.session.commit()