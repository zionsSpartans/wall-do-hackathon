## Deploy Infra Hosts
### Dependencias
- Filebeat
- Fail2ban [Recomendado]



## Deploy entorno de pruebas con Vagrant:
- Levantar las maquinas:
```
vagrant up
```

- Destruir las maquinas:
```
vagrant destroy
```

- Comprobar datos de acceso:
```
vagrant ssh-config
```
  - Conectar luego usando:
    - `ssh -i $key -l vagrant -p $port localhost`
    - `vagrant ssh $maquina` (no funciona bien con cygwin)
  - Dentro de cada maquina en /vagrant hay una copia de los ficheros de esta misma carpeta
    - Instalar paquete filebeat y configurar