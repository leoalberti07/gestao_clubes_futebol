from app import db

class Competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competicao = db.Column(db.String, nullable= True)
    colocacao = db.Column(db.Integer, nullable = True)
    vitorias = db.Column(db.Integer )