from flask import request
import requests
from flask_restful import Resource
from helpers.config import URL_SOLR

class BuscadorOcupacoes(Resource):
    def get(self):
        termo = request.args.get("q", "*:*")  # Pega o termo da query string
        params = {
            "q": f"titulo:*{termo}*",
            "wt": "json"
        }

        SOLR_QUERY_URL = f"{URL_SOLR}/select"

        response = requests.get(SOLR_QUERY_URL, params=params)

        if response.status_code == 200:
            return response.json(), 200
        else:
            return {"erro": "Falha na busca"}, 500

