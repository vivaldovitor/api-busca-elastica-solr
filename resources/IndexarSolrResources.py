from flask_restful import Resource
import requests
from .OcupacaoResources import dataset_ocupacao_csv
from helpers.database import db

class IndexarSolr(Resource):
    
    def post(self):

        ocupacoes = dataset_ocupacao_csv("/home/vivaldo/Documentos/estudos/gcsi/CBO2002-Ocupacao.csv")

        if not ocupacoes:
            return {"message": "Nenhum dado encontrado para indexar"}, 400
        
        try:
            # Indexar no Solr
            solr_url = "http://localhost:8000/solr/cbo_ocupacao_core/update?commit=true"
            headers = {"Content-Type": "application/json"}
            ocupacoes_json = [{"id": o.id, "titulo": o.titulo} for o in ocupacoes]

            response = requests.post(solr_url, json=ocupacoes_json, headers=headers)

            if response.status_code == 200:
                return {"message": "Dados Indexados no Solr com sucesso!"}, 200
            else:
                return {"message": "Falha ao indexar no Solr", "error": response.text}, 500
        
        except Exception as e:
            db.session.rollback()
            return {"message": "Ocorreu um erro ao tentar inserir os dados", "error": str(e)}, 500
