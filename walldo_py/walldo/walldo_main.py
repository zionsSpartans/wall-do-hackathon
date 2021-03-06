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
from acciones.desbaneos import revisa_baneos

def query():
    while True:
        query_main()

def scoring():
    while True:
        recoje_puntuaciones()
        time.sleep(180)

def unbans():
    while True:
        revisa_baneos()
        time.sleep(60)


def main():
    p1 = Process(target=query)
    p1.start()
    p2 = Process(target=scoring)
    p2.start()
    p3 = Process(target=unbans)
    p3.start()
    p1.join()
    p2.join()
    p3.join()

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

