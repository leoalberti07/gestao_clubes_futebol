from app import db
from datetime import datetime

class competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    numero_camisa = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(20), default="Ativo")
    valor_mercado = db.Column(db.Float, nullable=False)
    salario = db.Column(db.Float, nullable=False)

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)
    valor_transacao = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    data_transacao = db.Column(db.DateTime, nullable=False, default=datetime.now)
