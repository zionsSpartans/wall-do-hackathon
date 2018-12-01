ban = [{'rango': '200', 'tiempo': 60, 'cd':120}, {'rango': '400', 'tiempo': 180, 'cd': 360}]

def baneos(ip, puntuaciones):
    i = 0
    while i < len(ban):
        if str(puntuaciones) > ban[i]['rango']:
            baneo = {'ip': ip, 'tiempo': ban[i]['tiempo'], 'cd': ban[i]['cd']}
        elif str(puntuaciones) < ban[0]['rango']:
            baneo = 0
        i += 1

    return baneo

