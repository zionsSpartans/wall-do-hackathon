#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modulo para la recarga manual de la whitelist en BBDD

import sys
sys.path.append('/walldo')
from walldodb.whitelist import load_whitelist
from global_conf import whitelist_path

# Carga de IPs en la whitelist
try:
    load_whitelist(whitelist_path)
    print("Cargadas IPs en whitelist")
except Exception as e:
    print("No se ha podido cargar la whitelist: " + str(e))