from app import db

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