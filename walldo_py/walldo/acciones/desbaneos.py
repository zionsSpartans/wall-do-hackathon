from walldodb.configbd import conn
from acciones.ssh import desbaneo_ssh
import time
import datetime

# Batch temporal a ejecutar en segundo plano mientras se investiga como trabajar con trigger en mongo

# Recuperamos conector a BBBDD
bd = conn()
baneos = bd.baneos


def revisa_baneos():
    coleccion = baneos.find()
    for doc in coleccion:
        if doc['unban'] < datetime.datetime.now():
            ip = doc['ip']
            print(ip)
            desbaneo_ssh(ip)