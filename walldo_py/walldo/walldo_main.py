import elasticsearch.helpers
import time

from elasticsearch import Elasticsearch

elasticSource = elasticsearch.Elasticsearch([{"host": "localhost", "port": 9200}])
elasticDestination = elasticsearch.Elasticsearch([{"host": "localhost", "port": 9200}])
es = Elasticsearch()
res = es.search(index="filebeat*", body={"query": {"match_all": {}}})
#print de documentos para las pruebas
print("%d documents found" % res['hits']['total'])
scroll_size = res['hits']['total']
while (scroll_size > 0):
    for doc in res['hits']['hits']:
        if doc['_source']['source'] == "/var/log/auth.log":
            

        #print("%s) %s" % (doc['_id'], doc['_source']['system']))
        #es.delete(index="filebeat*", doc_type="doc", id=doc['_id'])

    #time.sleep(5)
    res = es.search(index="filebeat*", body={"query": {"match_all": {}}})

# elasticsearch.helpers.reindex(client=elasticSource, source_index="filebeat-6.4.2-2018.11.24", target_index="indice_principal", target_client=elasticDestination)
