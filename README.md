# DKIM Creator
Este programa ayuda a la creación automática de claves __DKIM__ en el servidor para los dominios que se indique. Además el programa sube de forma automática la clave a los registros del dominio en servidores que utilicen Odin Plesk por medio de __dns_utility__.

El programa ha sido probado en Centos 6 pero puede funcionar en cualquier otro que tenga instalado __opendkim__.

El programa es de gran ayuda ya que no se debe ir creando clave por clave y luego agregarlas a los __DNS__ de forma manual. Puede ser útil para administradores de sistemas que desean automatizar este proceso ahorrandoles muchas horas.

A este momento no soy un experto en Python por lo que el programa podría contener errores, bugs, problemas de seguridad entre otros.

## Requerimientos
- Sistema operativo basado en Linux
- opendkim
- Python 2.7 (No ha sido probado en Python 3)
- Plesk (opcional)

## Funcionalidades

- Creación de claves __DKIM__ de forma individual.
- Creación de claves __DKIM__ por volumen.
- Creación de nuevas zonas de nombre de dominio con valores __TXT__ en la que se agrega la clave publica de la clave __DKIM__.

## Licencia
- Mozilla Public License
- Version 2.0

Esta forma de código fuenta esta sujeta a los terminosde la Mozilla Public License, v. 2.0. Si una copia de la MPL no fue distribuida con este archivo, usted puede obtener una  en http://mozilla.org/MPL/2.0/.