from configbd import conn

bd = conn()


out = bd.puntuaciones.find_one()

print(out)
