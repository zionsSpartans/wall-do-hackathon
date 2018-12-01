alertas = [{'rango':'100'}, {'rango':'200'}]

def alert(ip, puntuaciones):
    if str(puntuaciones) > alertas[0]['rango'] and str(puntuaciones) < alertas[1]['rango']:
            alerta = "Ip: " + ip +" en el rango de alerta"
            return alerta
    else:
        return 0