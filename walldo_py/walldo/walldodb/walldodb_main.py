from walldodb.configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones
baneos = bd.baneos

# Objetos temporales para pruebas
# detectedip = { "ip": "10.0.13.1", "score": 35 }
# badip = {"ip": "10.0.13.1", "score": 10}
# niceip = {"ip": "10.0.13.1", "score": -5}


def update_score(ip_frommodule):
    # Recuperamos info de BBDD
    ip_indb = score.find_one({"ip": ip_frommodule["ip"]})
    # Si no habia info se realizara un insert con la puntuacion
    if ip_indb is None:
        new_score = ip_frommodule["score"]
        print("No existe en BBDD, insertamos puntuacion")
    else:
        new_score = ip_indb["score"] + ip_frommodule["score"]
        print("Existe en BBDD, actualizamos puntuacion")
    # PRINT PARA DEMO
    print("Antes: " + str(ip_indb))
    # Actualizamos en BBDD con la nueva puntuacion
    score.update_one({"ip": ip_frommodule["ip"]}, { "$set": { "score": new_score }},upsert=True)
    # PRINT PARA DEMO
    print("Despues: " + str(score.find_one({"ip": ip_frommodule["ip"]})))

def update_ban(ip, lastban, unbantime):
    # Recuperamos info de BBDD
    ip_indb = baneos.find_one({"ip": ip})
    # Si no habia info se realizara una entrada
    if ip_indb is None:
        baneos.update_one({"ip": ip}, { "$set": { "lastban": lastban, "unban" : unbantime }},upsert=True)
    else:
        print("Esta en BBDD")