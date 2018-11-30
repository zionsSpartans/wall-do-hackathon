import time
from queryAuth import queryauth
from elasticconfig import es
from queryIndices import queryIndices

#queryIndice() se encarga de devolver el indice mas antiguo con valores
indice = queryIndices()
if indice is not 0:
    res = es.search(index=indice, body={"query": {"match_all": {}}})
    print("%d documents found" % res['hits']['total'])
    scroll_size = res['hits']['total']
    while (scroll_size > 0):
        for doc in res['hits']['hits']:
            if doc['_source']['source'] == "/var/log/auth.log":
                queryauth(doc)
            es.delete(index=indice, doc_type="doc", id=doc['_id'])

        time.sleep(5)
        res = es.search(index=indice, body={"query": {"match_all": {}}})
        scroll_size = res['hits']['total']
