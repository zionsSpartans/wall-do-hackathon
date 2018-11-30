#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/walldo/walldodb')
from walldodb import update_score

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
##########################################################################################

def queryauth(doc):
    try:
        ssh_event = doc['_source']['system']['auth']['ssh']['event']
        if  ssh_event == "Accepted":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            detectedip = { "ip": ssh_ip, "score": -10 }
            update_score(detectedip)
        elif ssh_event == "Failed":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            detectedip = { "ip": ssh_ip, "score": 20 }
            update_score(detectedip)
    except:
        print("Patron no detectado")

