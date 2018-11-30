from walldodb.configbd import conn
from acciones import baneos, alertas
# Batch temporal a ejecutar en segundo plano mientras se investiga como trabajar con trigger en mongo

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

def recoje_puntuaciones():
    coleccion = score.find()
    for doc in coleccion:
        ip = doc['ip']
        puntuaciones = doc['score']
        print(ip + '-' + str(puntuaciones))
        if alert(str(puntuaciones)) == 0:
            ban = baneos(ip, str(puntuaciones))
            accion_baneo_ssh(ban)
        else:
            alert = alert(str(puntuaciones))
            accion_tg(alert)