#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
sys.path.append('/walldo')
from elastic.query_main import query_main

# Espera para permitir que Elastic arranque
# PDTE de sustituir por un healtcheck a una URL de elastic
print("Esperando 60 segundos para arrancar...")
time.sleep(60)
print("Arrancando!")

while True:
    query_main()