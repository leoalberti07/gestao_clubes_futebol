from app import db

class competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    historico = db.Column(db.Text, nullable=True)