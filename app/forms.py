from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from app.models import Jogador
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
        db.session.commit