from app import db

class competicoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    