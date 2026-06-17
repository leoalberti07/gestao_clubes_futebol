from app import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    historico = db.Column(db.String(500)) 

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'), nullable=False)

class competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)