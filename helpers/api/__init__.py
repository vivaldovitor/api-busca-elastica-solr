from flask_restful import Api

from resources.OcupacaoResources import InsertOcupacoes
from resources.IndexarSolrResources import IndexarSolr
from resources.BuscarOcupacoesResources import BuscadorOcupacoes

api = Api()

api.add_resource(InsertOcupacoes, "/insert_dataset")
api.add_resource(IndexarSolr, "/insert_dataset_in_solr")
api.add_resource(BuscadorOcupacoes, '/ocupacoes/buscar')