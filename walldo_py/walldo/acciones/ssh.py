import subprocess
import datetime
import time
from walldodb.walldodb_main import query_ban
from walldodb.walldodb_main import update_ban

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
    # Comprobamos si se debe banear
    if query_ban(ip_toban,actual_time):
        print("Hay que banear")
        unban_time = datetime.datetime.now() + datetime.timedelta(minutes=baneo)
        #### METER EN TRY
        # Update en BD
        update_ban(ip_toban,actual_time,unban_time)
        # Ejecuta ban
        baneo_ssh(ip_toban)
    else:
        print("No hay que banear")

