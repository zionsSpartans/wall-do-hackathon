import subprocess
import datetime
import time

# Modulo PDTE de utilizar directamente python con ansible API

hosts_path = "/walldo/hosts"

# Ejemplo de dict para pruebas
# [{'ip': 12, 'tiempo': '120', 'cd': '180'}]

# Funcion que a traves de un script auxiliar banea la IP que se le pasa.
#
# Ademas, insert en una tabla la fecha del baneo y la de desbaneo para poder llevar un control.
#
def accion_baneo_ssh(ssh_dict):
    ip_toban = ssh_dict["ip"]
    baneo = ssh_dict["tiempo"]
    # Ejecucion del script auxiliar
    torun = subprocess.Popen(["run_ban_ssh.sh", hosts_path, ip_toban], stdout=subprocess.PIPE)
    output , err = torun.communicate()
    # Print output ejecucion ansible
    print(output)
    # Guardamos fecha del baneo
    ban_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M")
    unban_time = datetime.datetime.now() + datetime.timedelta(minutes=baneo)
    unban_time = unban_time.strftime("%Y-%m-%d %H:%M")
    print(ban_time)
    print(unban_time)