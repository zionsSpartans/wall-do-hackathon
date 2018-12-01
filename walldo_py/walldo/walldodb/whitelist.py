from walldodb.configbd import conn
import os

# Recuperamos conector a BBBDD
bd = conn()
whitelist = bd.whitelist


# Func para comprobar si una IP esta whitelisted
def is_white(ip):
    # Recuperamos info de BBDD
    ip_inwhite = whitelist.find_one({"ip": ip})
    if ip_inwhite is None:
        return False
    else:
        return True


# Func para insertar IP en BBDD
def insert_whitelist(ip):
    whitelist.update_one({"ip": ip}, {"$set": {"ip": ip}}, upsert=True)


# Func para cargar fichero de IPs en BBDD
def load_whitelist(file):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        # Borramos datos previos
        whitelist.delete_many({})
        # Cargamos de nuevo el fichero en BBDD
        with open(file, 'r') as f:
            for line in f:
                insert_whitelist(line)
                print("IP añadida a la whitelist " + line)
    else:
        print("No hay IPs en la whitelist")
