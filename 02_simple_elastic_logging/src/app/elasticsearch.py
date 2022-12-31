import time
from datetime import datetime

import elastic_transport
from elasticsearch import Elasticsearch


def connect_elasticsearch():
    time.sleep(15)
    _es = None
    _es = Elasticsearch("http://elasticsearch:9200")
    return _es


class ESClient:
    def __init__(self):
        self.es = connect_elasticsearch()

    def startup(self):
        try:
            resp = self.es.info()
            print(resp)
        except Exception as e:
            print(f"An error occurred while connecting: {e}")

        doc = {
            "project": "Pythonic-API",
            "message": "Successfully established Elasticsearch connection from Python!",
            "timestamp": datetime.now(),
        }

        try:
            resp = self.es.index(index="init", id="1", document=doc)
        except elastic_transport.ConnectionError as e:
            print(f"Elasticsearch ConnectionError! \nMessage: {e}\n")
        except Exception as e:
            print(f"An error occured... {e}")
        else:
            print(resp["result"])
