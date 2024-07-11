# Lander
  
Este modulo es usado para conectar a Lander y ejecutar comandos.  

*Read this in other languages: [English](Manual_Lander.md), [Português](Manual_Lander.pr.md), [Español](Manual_Lander.es.md)*
  
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a Lander
  
Conectate a Lander
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Agrega tu apikey de Lander|API key de Lander|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|IP o host en el cual está corriendo Lander|IP o host en el cual está corriendo Lander|localhost|
|Puerto en el cual esta corriendo Lander|Puerto en el cual esta corriendo Lander|9999|
|Ruta del ejecutable de Rocketbot|Ruta donde se encuentra rocketbot.exe en el ambiente donde se ejecuta Lander.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/rocketbot.exe|
|Parámetros de línea de comandos|Parámetros extra que recibirá Rocketbot al momento de ejecutar los robots con Lander.|--log='log/path' --debug='false'|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Agregar robot a la cola
  
Agrega un robot a la cola de robots de Lander
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del robot|Nombre del robot que quieres agregar a la cola de Lander|MyRobot|
|Modo de ejecución del robot|||
|Parámetros de linea de comandos|Parámetros extras que recibira la linea de comando al ejecutar el robot.|--debug='false'|
|Datos extras del robot|Información extra que se quiera enviar al ejecutar el robot|{'times': 5, 'name': 'Jogn'}|
|Ruta de base de datos|Ruta donde se encuentra robot.db.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/robot.db|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Ejecutar bot
  
Permite correr un robot de la cola de robots de Lander
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del robot|ID del robot que quieres ejecutar|5|
|Modo de ejecución del robot|||
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
