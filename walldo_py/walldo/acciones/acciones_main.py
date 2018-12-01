from walldodb.configbd import conn
from acciones.baneos import baneos
from acciones.ssh import accion_baneo_ssh
from acciones.alertas import alert
from walldodb.whitelist import is_white
from walldodb.walldodb_main import update_score
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
        # Si la IP esta en al whitelist se pone la puntuacion a 0
        if is_white(ip):
            # Poner a 0
            print("IP en la whitelist, poniendo a 0: " + str(ip))
            ip_toreduce = {"ip": ip, "score": 0}
            update_score(ip_toreduce)
            puntuaciones = 0

        if alert(ip, str(puntuaciones)) == 0:
            ban = baneos(ip, str(puntuaciones))
            print('baneo')
            print(ban)
            accion_baneo_ssh(ban)
        else:
            alerta = alert(ip, str(puntuaciones))
            #Modulo pendiente de desarrollar
            print('En este punto se enviaria una alerta.')
            #accion_tg(alerta)