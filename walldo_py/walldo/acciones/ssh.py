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


hosts_path = "/walldo/hosts"

# Ejemplo de dict para pruebas
# {'ip': "14.14.14.14", 'tiempo': 60, 'cd': 180}


def baneo_ssh(ip_toban):
    # Ejecucion del script auxiliar
    torun = subprocess.Popen(["run_ban_ssh.sh", hosts_path, ip_toban], stdout=subprocess.PIPE)
    output , err = torun.communicate()
    # Print output ejecucion ansible
    print(output)


def accion_baneo_ssh(ssh_dict):
    ip_toban = ssh_dict["ip"]
    baneo = ssh_dict["tiempo"]
    cooldown = ssh_dict["cd"]
    # Guardamos fecha actual
    ban_time = datetime.datetime.fromtimestamp(time.time())
    ban_time_human = ban_time.strftime("%Y-%m-%d %H:%M")
    unban_time = datetime.datetime.now() + datetime.timedelta(minutes=baneo)
    unban_time_human = unban_time.strftime("%Y-%m-%d %H:%M")
    print(ban_time_human)
    print(unban_time_human)
    # Comprobamos si se debe banear
    query_ban(ip_toban,ban_time,unban_time,cooldown)


