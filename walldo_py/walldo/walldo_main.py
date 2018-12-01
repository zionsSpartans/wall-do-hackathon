#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
sys.path.append('/walldo')
from global_conf import whitelist_path
from walldodb.whitelist import load_whitelist
from elastic.query_main import query_main
from acciones.acciones_main import recoje_puntuaciones

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

while True:
    query_main()
    #recoje_puntuaciones()