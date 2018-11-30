from elastic.elasticconfig import es


def queryIndices():
    var = sorted(es.indices.get_alias("file*"))
    i = 0
    while i < len(var):
        indice = var[i]
        res = es.search(index=indice, body={"query": {"match_all": {}}})
        if res['hits']['total'] > 0:
            print(indice)
            return indice
        elif i == len(var):
            return 0
        else:
            print("vacio")
        i += 1
