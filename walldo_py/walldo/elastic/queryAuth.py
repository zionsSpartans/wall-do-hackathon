from elasticsearch import Elasticsearch

def queryauth(doc):
    #print(doc['_source']['system'])

    try:
        if  doc['_source']['system']['auth']['ssh']['event'] == "Accepted":
            print("Accepted")
        if doc['_source']['system']['auth']['ssh']['event'] == "Failed":
            print("Failed")
    except Exception as e:
        print(e)
    #    print("Vacio")
    #if  doc['_source']['system']['auth']['ssh']['event'] == "Accepted":
    #    print("Accepted")
    #if doc['_source']['system']['auth']['ssh']['event'] == "Failed":
    #print("Failed")
