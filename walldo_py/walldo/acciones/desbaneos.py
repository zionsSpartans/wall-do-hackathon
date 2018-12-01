from walldodb.configbd import conn
from acciones.ssh import desbaneo_ssh
from walldodb.whitelist import is_white
from walldodb.walldodb_main import update_score
import datetime

# Batch temporal a ejecutar en segundo plano mientras se investiga como trabajar con trigger en mongo

# Recuperamos conector a BBBDD
bd = conn()
baneos = bd.baneos


def revisa_baneos():
    coleccion = baneos.find()
    for doc in coleccion:
        ip = doc['ip']
        if is_white(ip):
            # Poner a 0
            print("IP en la whitelist, poniendo a 0: " + str(ip))
            ip_toreduce = {"ip": ip, "score": 0}
            update_score(ip_toreduce)
            # Eliminar entrada de la coleccion de baneos
            baneos.delete_one({"ip": ip})
            desbaneo_ssh(ip)
        elif doc['unban'] < datetime.datetime.now():
            desbaneo_ssh(ip)