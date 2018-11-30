#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/root/wall-do-hackathon/walldo_py/walldo')
import time

from elastic.query_main import query_main

time.sleep(60)
while True:
    query_main()
