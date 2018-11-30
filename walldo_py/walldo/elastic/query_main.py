import time
#import sys
#sys.path.append('/walldo/elastic')
from elastic.queryAuth import queryauth
from elastic.elasticconfig import es
from elastic.queryIndices import queryIndices


def query_main():
    #queryIndice() se encarga de devolver el indice mas antiguo con valores
    indice = queryIndices()
    if indice is not 0:
        try:
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
        except:
            time.sleep(5)


