# Conexión entre un adaptador USB a 485
## Instalación de driver
Para llevar a cabo esta conexión habrá que dejar instalado el driver universal de windows que se encuentra en este enlace `https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads` (si estamos en windows, si estamos en otro sistema operativo, el correspondiente)
Una vez instalado podremos observar que el dispositivo ya aparece en el `Administrador de dispositivos` de nuestro equipo en el apartado de `Puertos serie y COM`

## Instalación de librerías
Para realizar la prueba instalaremos la librería o librerías necesarias. Todas ellas se encuentran en el archivo `requirements.txt` 
Para realizar la instalación de dichas librerías emplearemos el comando
```bash
pip install -r requirements .txt
```
Una vez instaladas ya podremos ejecutar el programa de python sin ningún inconveniente
