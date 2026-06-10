from flask_wtf import FlaskForm
from wtforms import   StringField, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

from app import db
from app.models import Competicoes
class CompeticoesForm(FlaskForm):
    competicao = SelectField("Competição: ",choices=[
            ("brasileirao", "Brasileirão"),
            ("libertadores", "Libertadores"),
            ("copa_brasil", "Copa do Brasil")], )
    colocacao = IntegerField("Colocação: ", validators=[DataRequired(), NumberRange(min=1, max=20)])
    vitorias = IntegerField("Numero de vitorias em fase de mata-mata: ", validators=[DataRequired(), NumberRange(min=0, max=6 )])

    btnSubmit = SubmitField("Enviar")

    def save(self):
        list_competicoes =  Competicoes(
            competicao = self.competicao.data , 
            colocacao = self.colocacao.data,
            vitorias = self.vitorias.data
        )

        db.session.add(list_competicoes)
        db.session.commit()
