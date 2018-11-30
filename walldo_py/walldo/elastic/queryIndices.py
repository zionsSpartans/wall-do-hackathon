from elasticconfig import es

def queryIndices():

    var = es.indices.get_alias("file*")
    indice = list(var.keys())[0]
    res = es.search(index=indice, body={"query": {"match_all": {}}})

    if res is None:
        return ""
    else:
        return indice