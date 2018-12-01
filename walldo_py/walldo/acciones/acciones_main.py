from walldodb.configbd import conn
from acciones.baneos import baneos
from acciones.ssh import accion_baneo_ssh
# Batch temporal a ejecutar en segundo plano mientras se investiga como trabajar con trigger en mongo

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

##########################################################################################
#
#Funcion utilizada para el recojer la coleccion de las ips en mongodb. Una vez tienes una tupla se estudia
#si esta ip recogida tiene que tener una medida asociada(alerta, baneo, desbaneo,...)
#
#alert(puntuaciones) -> Funcion utilizada para determinar las medidas menos restrictivas. Si esta funcion devuelve 0
# entendemos que hablamos de un baneo.
#
#baneos(ip, puntuaciones) -> Funcion utilizada para determinar que tipo de baneo se va a imponer.
#
#Las funciones previamente comentadas devuelven una coleccion que se pasara al module que realiza la medida
#
##########################################################################################
def recoje_puntuaciones():
    coleccion = score.find()
    for doc in coleccion:
        ip = doc['ip']
        puntuaciones = doc['score']
        if alert(str(puntuaciones)) == 0:
            ban = baneos(ip, str(puntuaciones))
            print('baneo')
            accion_baneo_ssh(ban)
        else:
            alert = alert(str(puntuaciones))
            print('alerta')
            accion_tg(alert)