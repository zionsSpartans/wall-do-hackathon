from elasticsearch import Elasticsearch

def queryauth(doc):
    print(doc['_source']['system'])

    #if ssh_event is None:
    #    print("Vacio")
    #if  doc['_source']['system']['auth']['ssh']['event'] == "Accepted":
    #    print("Accepted")
    #if doc['_source']['system']['auth']['ssh']['event'] == "Failed":
    #print("Failed")
