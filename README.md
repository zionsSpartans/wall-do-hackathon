# Wall-do
Repositorio para el desarrollo de Wall-do durante Hackathon de Cybercamp 2018.

![](notas/imgs/500_logo_walldo_ladrillo.png)

**Wall-do** es una herramienta inspirada en fail2ban, pero de forma distribuida, para la detección y prevención de ataques.

Basándose en la información recopilada de los logs en los diferentes hosts se realiza un análisis de las IPs que han interactuado con los mismos. Este análisis se basa en la frecuencia de interacción, comportamiento (p.e: intentos de acceso fallidos) y el contraste con blacklist públicas.

Tras asignar una puntuación, en base a esta se determinan las acciones a realizar, que pueden ir desde una alerta hasta un baneo permanente.

## Deploy Wall-do
### Dependencias
- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/#install-compose)

### Despliegue
0. Clonar repo:
  ```bash
  git clone git@github.com:zionsSpartans/wall-do-hackathon.git
  ```
1. Configurar credenciales:
```bash
cd wall-do-hackathon
cp -rp mongodb/mongocreds.env.template mongodb/mongocreds.env
vim mongodb/mongocreds.env # Rellenar credenciales BBDD
cp -rp walldo_py/walldo/walldodb/configbd.py.template walldo_py/walldo/walldodb/configbd.py
vim walldo_py/walldo/walldodb/configbd.py # Rellenar credenciales BBDD (las mismas que antes!!)
```

2. Configurar conexion a Elasticsearch:
  - Si se va a utilizar el stack levantado en docker:
    ```bash
    echo "ELK_VERSION=6.4.2" >> .env # Seleccionar la versión a utilizar de Elastic
    mv walldo_py/walldo/elastic/elasticconfig.py.template walldo_py/walldo/elastic/elasticconfig.py
    ```
  - Si se va a utilizar un Elastic propio:
    ```bash
    mv walldo_py/walldo/elastic/elasticconfig.py.template walldo_py/walldo/elastic/elasticconfig.py
    vim walldo_py/walldo/elastic/elasticconfig.py
    ```

3. Configuraciones varias:
   - Desde el fichero 'walldo_py/walldodb/global_conf.py' se pueden
     configurar las puntuaciones de los modulos.
   - La ruta donde se encuentra el fichero de whitelist.
     - Este fichero unicamente debe contener el listado de IPs.
     - Estas IPs se cargan en BBDD al arrancar la aplicación.

4. Configurar hosts a los que debe conectar ansible:
   ```bash
   vim walldo_py/walldo/hosts
   ```
      - [Info acerca del inventario en Ansible](https://docs.ansible.com/ansible/2.4/intro_inventory.html)

5. Arrancar con docker compose:
```bash
docker-compose up # Usar '-d' si queremos que arranque en segundo plano 
```
  - Si no se va a usar el stack de ELK comentar en el docker-compose.

## Estructura del repositorio

- walldo_py:
    - Directorio del contenedor python
    - Dentro de este directorio está el directorio 'walldo' que contiene el código de la aplicación
    
- Directorios contenedores stack ELK:
    - elasticsearch
    - extensions 
    - kibana 	
    - logstash 

- mongodb:
    - Directorio contenedores mongo
	
- notas:
    - Anotaciones del equipo

- vagrantHosts: 
    - Material para desplegar las VMs

- Presentacion_Hackathon:
    - Presentaciones utilizadas durante la competición