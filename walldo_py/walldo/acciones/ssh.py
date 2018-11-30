import subprocess
import datetime
import time
from walldodb.walldodb_main import query_ban

# Modulo PDTE de utilizar directamente python con ansible API
#
# Un script auxiliar se encarga de banear la IP que se le pasa.
#
# Ademas, se realiza un insert en una tabla la fecha del baneo y la de desbaneo para poder llevar un control.
#

# Ejecucion del script auxiliar
def baneo_ssh(ip_toban):
    hosts_path = "/walldo/hosts"
    torun = subprocess.Popen(["run_ban_ssh.sh", hosts_path, ip_toban], stdout=subprocess.PIPE)
    output , err = torun.communicate()
    # Print output ejecucion ansible
    print(output)


# Ejemplo de dict para pruebas
# {'ip': "14.14.14.14", 'tiempo': 60, 'cd': 180}

def accion_baneo_ssh(ssh_dict):
    ip_toban = ssh_dict["ip"]
    baneo = ssh_dict["tiempo"]
    cooldown = ssh_dict["cd"]
    # Guardamos fecha actual
    actual_time = datetime.datetime.fromtimestamp(time.time())
    actual_time_human = ban_time.strftime("%Y-%m-%d %H:%M")
    unban_time = datetime.datetime.now() + datetime.timedelta(minutes=baneo)
    unban_time_human = unban_time.strftime("%Y-%m-%d %H:%M")
    print(actual_time_human)
    print(unban_time_human)
    # Comprobamos si se debe banear
    if query_ban(ip_toban,actual_time,unban_time,cooldown):
        print("Hay que banear")
    else:
        print("No hay que banear")

