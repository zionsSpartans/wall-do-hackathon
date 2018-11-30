from configbd import conn

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

