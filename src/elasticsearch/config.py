from elasticsearch import Elasticsearch, helpers

ES_HOST = "http://localhost:9200"
ES_INDEX = "threatharvester"

# Connect to Elasticsearch
es = Elasticsearch(ES_HOST)
