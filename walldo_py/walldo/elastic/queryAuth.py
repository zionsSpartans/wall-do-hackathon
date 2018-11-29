from walldodb import update_score

def queryauth(doc):
    try:
        ssh_event = doc['_source']['system']['auth']['ssh']['event']
        if  ssh_event == "Accepted":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            update_score(ssh_ip, -10)
        elif ssh_event == "Failed":
            ssh_ip = doc['_source']['system']['auth']['ssh']['ip']
            update_score(ssh_ip, 20)
    except:
        print("")

