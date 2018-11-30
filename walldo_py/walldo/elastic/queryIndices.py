from elasticconfig import es

i = 0

def queryIndices():
    var = sorted(es.indices.get_alias("file*"))
    while i < len(var):
        indice = var[i]
        res = es.search(index=indice, body={"query": {"match_all": {}}})
        if res['hits']['total'] > 0:
            print(indice)
            return indice
        ++i