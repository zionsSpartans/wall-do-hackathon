from walldodb.configbd import conn
import time
import datetime

# Batch temporal a ejecutar en segundo plano mientras se investiga como trabajar con trigger en mongo

# Recuperamos conector a BBBDD
bd = conn()
score = bd.baneos


def revisa_baneos():
    coleccion = score.find()
    for doc in coleccion:
        if doc['unban'] < datetime.datetime.now():
            print("prueba")