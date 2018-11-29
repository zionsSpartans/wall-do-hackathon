from configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

# Objetos temporales para pruebas
detectedip = {"ip": "10.0.13.1", "score": 35}
badip = {"ip": "10.0.13.1", "score": 10}
niceip = {"ip": "10.0.13.1", "score": -5}

# Insert simple
def simple_insert_score(detectedip):
  # Insert del documento en la tabla puntuaciones
  score.insert_one(detectedip)

def update_score(detectedip):
  ip_tofind = detectedip[2]
  score.find_one()






### Testing funciones
insert_score(detectedip)