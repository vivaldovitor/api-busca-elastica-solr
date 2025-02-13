from helpers.database import db
from flask_restful import fields

ocupacaoField = {
    'id': fields.Integer,
    'titulo': fields.String
}

class Ocupacao(db.Model):
    __tablename__ = "ocupacoes_tb"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
