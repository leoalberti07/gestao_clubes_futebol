from app import db
from datetime import datetime

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    historico = db.Column(db.String(500)) 
    salario = db.Column(db.Float, nullable=False)

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)
    valor_transacao = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    data_transacao = db.Column(db.DateTime, nullable=False, default=datetime.now)

class Competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competicao = db.Column(db.String, nullable= True)
    colocacao = db.Column(db.Integer, nullable = True)
    premiacao = db.Column(db.Integer, nullable = True)
    num_jogos = db.Column(db.Integer, nullable = True)
    vitorias = db.Column(db.Integer)
    derrotas = db.Column(db.Integer)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'), nullable=False)

