#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/andoniaf/zionSpartans/wall-do-hackathon/walldo_py/walldo/walldodb')

from walldodb import update_score

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
        print("")

