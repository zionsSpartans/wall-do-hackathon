alertas = [{'rango':'100'}, {'rango':'300'}]

def baneos(ip, puntuaciones):
    i = 0
    while i < len(alertas):
        if str(puntuaciones) < alertas[i]['rango']:
            alert = [{'ip': ip}, {'tiempo': alertas[i]['tiempo']}, {'cd': alertas[i]['cd']}]
            return alert
        i += 1

    return 0
