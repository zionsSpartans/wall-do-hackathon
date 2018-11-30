#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
<<<<<<< HEAD
sys.path.append('/root/wall-do-hackathon/walldo_py/walldo')
import time

from elastic.query_main import query_main

time.sleep(60)
=======
sys.path.append('/walldo')
from elastic.query_main import query_main

# Espera para permitir que Elastic arranque
# PDTE de sustituir por un healtcheck a una URL de elastic
print("Esperando 60 segundos para arrancar...")
time.sleep(60)
print("Arrancando!")

>>>>>>> b3f325f7cb93effad15015051e08a212a6aa9b10
while True:
    query_main()
