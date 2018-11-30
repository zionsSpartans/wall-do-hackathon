# Wall-do
Repositorio para el desarrollo de Wall-do durante Hackathon de Cybercamp 2018.

![](notas/imgs/500_logo_walldo_ladrillo.png)

**Wall-do** es una herramienta inspirada en fail2ban, pero de forma distribuida, para la detección y prevención de ataques.

Basándose en la información recopilada de los logs en los diferentes hosts se realiza un análisis de las IPs que han interactuado con los mismos. Este análisis se basa en la frecuencia de interacción, comportamiento (p.e: intentos de acceso fallidos) y el contraste con blacklist públicas.

Tras asignar una puntuación, en base a esta se determinan las acciones a realizar, que pueden ir desde una alerta hasta un baneo permanente.

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