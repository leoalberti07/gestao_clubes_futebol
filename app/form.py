from flask_wtf import FlaskForm
from wtforms import  StringField, FloatField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, ValidationError,InputRequired


from app.models import *
from app import db


class CompeticoesForm(FlaskForm):
    competicao = StringField("Competições: ", validators=[DataRequired()])
    colocacao = IntegerField("Colocação: ", validators=[DataRequired(), NumberRange(min=0, max=1000)])
    premiacao = FloatField("Premiação: ", validators=[DataRequired(),NumberRange(min=0, max=1000000000000)])
    num_jogos = IntegerField("Número de jogos do campeonato: ", validators=[DataRequired(),NumberRange(min=0, max=1000)])
    vitorias =  IntegerField("Numero de vitorias: ", validators=[InputRequired(),NumberRange(min=0, max=1000)])
    empates =  IntegerField("Numero de empatesS: ", validators=[InputRequired(),NumberRange(min=0, max=1000)])
    derrotas = IntegerField("Numero de derrotas: ", validators=[InputRequired(),NumberRange(min=0, max=1000)])
    
    
    btnSubmit = SubmitField("Enviar")

    def save(self):
        list_competicoes =  Competicoes(
            competicao = self.competicao.data , 
            colocacao = self.colocacao.data,
            premiacao = self.premiacao.data,
            num_jogos = self.num_jogos.data,
            vitorias = self.vitorias.data,
            derrotas = self.derrotas.data,
            empates = self.empates.data
        )

        financias_competição = Transacao(
            tipo = 'RECEITA',
            valor_transacao = self.premiacao.data,
            descricao = 'PREMIACAO'
            )

        db.session.add(list_competicoes)
        db.session.commit()
        
        db.session.add(financias_competição)
        db.session.commit()



    def validate_competicao(self, field):
        caracteres = "@*?!'^+%&/()=}][{$#"
        for car in self.competicao.data:
            if car in caracteres:
                raise ValidationError(f"Erro,  não pode conter caracter especiais ")
    
    
    def validate_num_jogos(self, field):
        if field.data < self.vitorias.data + self.derrotas.data + self.empates.data:
            raise ValidationError(
                "O número de jogos não pode ser menor que do que a soma de vitorias, empates e derrotas."
            )
    

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

class JogadorForm(FlaskForm):
    nome_atleta = StringField('Nome', validators=[DataRequired()])
    posicao_atleta = SelectField('Posição', choices=[('GOL','GOL'),('ZAG','ZAG'),('LAT','LAT'),('MC','MC'),('MEI','MEI'),('PE','PE'),('PD','PD'),('ATA','ATA')])
    situacao_atleta = SelectField('Situação', choices=[('ATIVO','ATIVO'),('EMPRESTADO','EMPRESTADO'),('LESIONADO','LESIONADO'),('INATIVO','INATIVO')])
    historico_atleta = TextAreaField('Histórico inicial')
    salario = FloatField('Salário', validators=[DataRequired(), NumberRange(min=1621, max=100000000)])
    submit = SubmitField('Cadastrar')

    def save(self):

        jogador = Jogador(
            nome_atleta = self.nome_atleta.data,
            posicao_atleta = self.posicao_atleta.data,
            situacao_atleta = self.situacao_atleta.data,
            historico_atleta = self.historico_atleta.data,
            salario = self.salario.data
        )

        db.session.add(jogador)
        db.session.commit()



class TransferenciasForm(FlaskForm):
    nome_atleta = StringField('Nome', validators=[DataRequired()])
    posicao_atleta = SelectField('Posição', choices=[('GOL','GOL'),('ZAG','ZAG'),('LAT','LAT'),('MC','MC'),('MEI','MEI'),('PE','PE'),('PD','PD'),('ATA','ATA')])
    clube = StringField('Clube anterior', validators=[DataRequired()])
    valor = FloatField("Valor de Transferencia",validators=[DataRequired()])
    salario = FloatField("Salário",validators=[DataRequired(),NumberRange(min=1621, max=100000000)])   
    
    submit = SubmitField("Enviar") 


    def save(self):
        transferencia = Transferencias(
            nome_atleta = self.nome_atleta.data,
            posicao_atleta = self.posicao_atleta.data,
            clube =self.clube.data,
            valor=self.valor.data,
            salario = self.salario.data,
     )
        transacao = Transacao(
            tipo = 'DESPESA',
            valor_transacao = self.valor.data,
            descricao = f'COMPRA ATLETA: {self.nome_atleta.data}',
            
        )

        jogador = Jogador(
            nome_atleta = self.nome_atleta.data,
            posicao_atleta = self.posicao_atleta.data,
            situacao_atleta = 'jogador transferido',
            historico_atleta = f"clube anterior: {self.clube.data}",
            salario = self.salario.data
        )

        db.session.add(jogador)
        db.session.add(transacao)
        db.session.add(transferencia)
        db.session.commit()    


    def validate_nome_atleta(self, field):
        caracteres = "@*?!'^+%&/()=}][{$#"
        for car in self.nome_atleta.data:
            if car in caracteres:
                raise ValidationError(f"Erro,  não pode conter {car} ")
    def validate_clube(self, field):
        caracteres = "@*?!'^+%&/()=}][{$#"
        for car in self.clube.data:
            if car in caracteres:
                raise ValidationError(f"Erro,  não pode conter {car} ")
    