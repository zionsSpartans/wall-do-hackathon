#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
#sys.path.append('/walldo/walldodb')
from walldodb.walldodb_main import update_score
from walldodb.whitelist import is_white
from global_conf import *

##########################################################################################
#
#Funcion utilizada para el tratamiento de los logs de auth.log. Los logs que nos interesan
#son aquellos que dan un acierto de contraseña o un fallo de contraseña.
#
#ssh_event -> variable que nos indica que evento es el que estamos tratando (Accepted password,
#             Failed password)
#
#ssh_ip -> variable que guarda la ip del documento estudiado
#
# TODO:
# - Permitir seleecionar que otros users pueden tener diferente puntuacion
#
##########################################################################################

def queryauth(doc):
    try:
        ssh_event = doc['_source']['system']['auth']['ssh']['event']

        if  ssh_event == "Accepted":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            detectedip = { "ip": ssh_ip, "score": ssh_accepted_score }
            print("Patron Accepted detectado")
            update_score(detectedip)
        elif ssh_event == "Failed":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            ssh_user = doc['_source']['system']['auth']['user']

            # Si la IP esta en al whitelist se corta la funcion
            if is_white(ssh_ip):
                # Salir
                print("IP en la whitelist: " + str(ssh_ip))
                return 0

            if ssh_user == "root":
                detectedip = { "ip": ssh_ip, "score": ssh_failed_root_score }
            else:
                detectedip = {"ip": ssh_ip, "score": ssh_failed_score}
            print("Patron Failed detectado")
            update_score(detectedip)

    except:
        print("Patron no detectado")


