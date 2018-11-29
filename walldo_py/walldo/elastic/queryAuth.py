from elasticsearch import Elasticsearch

def queryauth(doc):
    ssh_event = doc['_source']['system']['auth']['ssh']['event']

    if ssh_event is not None:
        print("Vacio")
    if  ssh_event == "Accepted":
        print("Accepted")
    if ssh_event == "Failed":
        print("Failed")
