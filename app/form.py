from flask_wtf import FlaskForm
from wtforms import   StringField, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

from app import db
from app.models import Competicoes
class CompeticoesForm(FlaskForm):
    time = StringField("Nome do time: ", validators=[DataRequired()])
    competicao = StringField("Competições: ", validators=[DataRequired()])
    num_jogos = IntegerField("Número de jogos: ", validators=[DataRequired(), NumberRange()])
    colocacao = IntegerField("Colocação: ", validators=[DataRequired(), NumberRange(min=0)])
    premiacao = FloatField("Premiação: ", validators=[DataRequired(),NumberRange(min=0)])
    vitorias = IntegerField("Numero de vitorias: ", validators=[DataRequired(),NumberRange(min=0 )])
    derrotas = IntegerField("Numero de derrotas: ", validators=[DataRequired(),NumberRange(min=0 ) ])
    
    
    btnSubmit = SubmitField("Enviar")

    def save(self):
        list_competicoes =  Competicoes(
            time = self.time.data,
            competicao = self.competicao.data , 
            colocacao = self.colocacao.data,
            vitorias = self.vitorias.data,
            derrotas = self.derrotas.data,
            num_jogos = self.num_jogos.data,
            premiacao = self.premiacao.data
        )

        db.session.add(list_competicoes)
        db.session.commit()
