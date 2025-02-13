from dotenv import load_dotenv
import os

load_dotenv(".env")

URL_SOLR=os.getenv("URL_SOLR", "http://localhost:8000/solr/cbo_ocupacao_core")