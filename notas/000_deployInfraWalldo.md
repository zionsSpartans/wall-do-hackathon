## Deploy Infra Wall-do
### Dependencias
- [Instalar Docker](https://docs.docker.com/install/)
- [Instalar docker-compose](https://docs.docker.com/compose/install/#install-compose)
- Clonar repo

### Despliegue
1. Configurar credenciales:
```bash
cp -rp mongodb/mongocreds.env.template mongodb/mongocreds.env
vim mongodb/mongocreds.env
cp -rp walldo_py/walldo/walldodb/configbd.py.template walldo_py/walldo/walldodb/configbd.py
vim walldo_py/walldo/walldodb/configbd.py
```

2. Arrancar con docker compose:
```bash
docker-compose up # Usar '-d' si queremos que arranque en segundo plano 
```


----

### Info
- Todos los contenedores estan en la misma red
  - Se pueden comunicar entre ellos por el nombre del servicio:
  ```bash

  ```


### walldo_py
- Contenedor con python + SSH
- Es donde se ejecuta Walldo y desde donde se lanzaran los comandos via SSH al resto de hosts.


### MongoDB
- 'mongo' es la bbdd y 'mongo-express' una interfaz gráfica:
  - Volumen para datos persistentes
  
### ELK
- Fork del repo [docker-ELK](https://github.com/deviantony/docker-elk)
- De momento no usamos logstash, por lo que esta comentado en el compose.

