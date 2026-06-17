from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class JogadorForm(FlaskForm):
    nome_atleta = StringField('Nome', validators=[DataRequired()])
    posicao_atleta = SelectField('Posição', choices=[('GOL','GOL'),('ZAG','ZAG'),('LAT','LAT'),('MC','MC'),('MEI','MEI'),('PE','PE'),('PD','PD'),('ATA','ATA')])
    situacao_atleta = SelectField('Situação', choices=[('ATIVO','ATIVO'),('EMPRESTADO','EMPRESTADO'),('LESIONADO','LESIONADO'),('INATIVO','INATIVO')])
    historico_atleta = TextAreaField('Histórico inicial')
    submit = SubmitField('Cadastrar')