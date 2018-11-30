from elasticconfig import es

def queryIndices():
    var = es.indices.get_alias("file*")
    sorted(var)
    indice = list(var.keys())[0]
    res = es.search(index=indice, body={"query": {"match_all": {}}})
    return indice
