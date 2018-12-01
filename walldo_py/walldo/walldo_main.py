#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time
import sys
sys.path.append('/walldo')
from global_conf import whitelist_path
from walldodb.whitelist import load_whitelist
from elastic.query_main import query_main
from acciones.acciones_main import recoje_puntuaciones

def proceso1():
    while True:
        query_main()

def proceso2():
    while True:
        recoje_puntuaciones()
        time.sleep(180)


def main():
    p1 = Process(target=proceso1)
    p1.start()
    p2 = Process(target=proceso2)
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    # Espera para permitir que Elastic arranque
    # PDTE de sustituir por un healtcheck a una URL de elastic
    print("Esperando 60 segundos para arrancar...")
    time.sleep(60)
    print("Arrancando!")

    # Carga de IPs en la whitelist
    try:
        load_whitelist(whitelist_path)
        print("Cargadas IPs en whitelist")
    except Exception as e:
        print("No se ha podido cargar la whitelist: " + str(e))

    main()

