from walldodb.configbd import conn

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
    with open(file, 'r') as f:
        empty = True
        for line in f:
            empty = False
            insert_whitelist(line)
            print("IP añadida a la whitelist " + line)
        if empty:
            print("No hay IPs en la whitelist")
