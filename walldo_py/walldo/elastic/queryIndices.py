from elasticconfig import es

def queryIndices():
    var = es.indices.get_alias("file*")
    indice = list(var.keys())[0]
    print(indice)

