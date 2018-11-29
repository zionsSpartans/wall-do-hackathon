from configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

# Objetos temporales para pruebas
detectedip = { "ip": "10.0.13.1", "score": 35 }
badip = {"ip": "10.0.13.1", "score": 10}
niceip = {"ip": "10.0.13.1", "score": -5}



def update_score(detectedip):
  # Recuperamos info de BBDD
  ip_indb = score.find_one({"ip": detectedip["ip"]})
  new_score = ip_indb["score"] + detectedip["score"]
  print(ip_indb)
  score.update_one({"ip": detectedip["ip"]}, { "$set": { "score": new_score }})
  print(score.find_one({"ip": detectedip["ip"]}))





### Testing funciones
insert_score(detectedip)