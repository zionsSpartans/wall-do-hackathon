from configbd import conn

# Recuperamos conector a BBBDD
bd = conn()
score = bd.puntuaciones

# Objeto temporal para pruebas
detectedip = {"ip": "10.0.13.1", "score": 35}

def insert_score(detectedip):
  # Insert del documento en la tabla puntuaciones
  score.insert_one(detectedip)








### Testing funciones
insert_score(detectedip)