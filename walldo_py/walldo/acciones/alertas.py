alertas = [{'rango':'100'}, {'rango':'200'}]

def alert(ip, puntuaciones):
    if str(puntuaciones) > alertas[0]['rango'] and str(puntuaciones) < alertas[1]['rango']:
            alerta = "Ip: " + ip +" en el rango de alerta"
            return 1
    elif str(puntuaciones) > alertas[1]['rango']:
        return 2
    else:
        return 0