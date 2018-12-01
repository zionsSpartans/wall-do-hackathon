#!/bin/sh

# Script auxiliar basando que a traves de ansible desbanea la IP pasada en todos los nodos configurados en el hosts

hosts_path="$1"
ip_toban="$2"

ansible -i ${hosts_path} -m iptables -a "chain=INPUT source=$ip_toban jump=DROP state=absent" -b  all
