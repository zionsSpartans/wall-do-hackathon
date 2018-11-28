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
  - Conectar luego usando `ssh -i $key -l vagrant -p $port localhost`
  - Dentro de cada maquina en /vagrant hay una copia de los ficheros de esta misma carpeta
