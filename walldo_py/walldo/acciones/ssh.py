import subprocess


# PDTE utilizar directamente python con ansible API

hosts_path = "/walldo/hosts"

# Funcion que a traves de un script auxiliar banea la IP que se le pasa.
#
# Ademas, insert en una tabla la fecha del baneo y la de desbaneo para poder llevar un control.
def accion_baneo_ssh(ssh_dict):
    ip_toban = ssh_dict["ip"]
    torun = subprocess.Popen(["run_ban_ssh.sh", hosts_path, ip_toban], stdout=subprocess.PIPE)
    output , err = p.communicate()
    print(output)


