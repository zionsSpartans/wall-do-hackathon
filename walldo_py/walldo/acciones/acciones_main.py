from walldodb.configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

def recoje_puntuaciones():
    coleccion = score.find()
    for doc in coleccion:
        ip = doc['ip']
        puntuaciones = doc['score']
        print(ip + '-' + str(puntuaciones))