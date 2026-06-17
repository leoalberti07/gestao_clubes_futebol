from flask_wtf import FlaskForm
from wtforms import  StringField, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError

from app import db
from app.models import Competicoes
class CompeticoesForm(FlaskForm):
    competicao = StringField("Competições: ", validators=[DataRequired()])
    colocacao = IntegerField("Colocação: ", validators=[DataRequired(), NumberRange(min=0, max=46)])
    premiacao = FloatField("Premiação: ", validators=[DataRequired(),NumberRange(min=0, max=1000000000000)])
    num_jogos = IntegerField("Número de jogos do campeonato: ", validators=[DataRequired()])
    vitorias = IntegerField("Numero de vitorias: ", validators=[DataRequired()])
    derrotas = IntegerField("Numero de derrotas: ", validators=[DataRequired()])
    
    
    btnSubmit = SubmitField("Enviar")

    def save(self):
        list_competicoes =  Competicoes(
            competicao = self.competicao.data , 
            colocacao = self.colocacao.data,
            premiacao = self.premiacao.data,
            num_jogos = self.num_jogos.data,
            vitorias = self.vitorias.data,
            derrotas = self.derrotas.data
        )



        db.session.add(list_competicoes)
        db.session.commit()

    def validate_competicao(self, field):
        caracteres = "@*?!'^+%&/()=}][{$#"
        for car in self.competicao.data:
            if car in caracteres:
                raise ValidationError(f"Erro,  não pode conter {car} ")


    
    
    
    def validate_num_jogos(self, field):
        if field.data < self.vitorias.data + self.derrotas.data:
            raise ValidationError(
                "O número de jogos não pode ser menor que vitórias + derrotas."
            )
    
