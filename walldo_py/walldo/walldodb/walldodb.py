from configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

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
    else:
        new_score = ip_indb["score"] + ip_frommodule["score"]
    # PRINT PARA DEMO
    print("Antes: " + str(ip_indb))
    # Actualizamos en BBDD con la nueva puntuacion
    score.update_one({"ip": ip_frommodule["ip"]}, { "$set": { "score": new_score }},upsert=True)
    # PRINT PARA DEMO
    print("Despues: " + str(score.find_one({"ip": ip_frommodule["ip"]})))

