#!/usr/bin/python
# -*- coding: utf-8 -*-
# Vars
## Directorio donde se encuentran los archivos de claves de openDKIM
base_dir = '/etc/opendkim/'
## Directorio donde se encuentran los dominios que han sido dados de alta en Plesk, estos se utilizan para confirmar si un dominio fue dado de alta en el panel, también permite una mejor integración con otros sistemas
domains_dir = '/var/qmail/mailnames/'
## s = Si, n = No, Dependiendo de la opción se verifica o no si el dominio existe o no de esta manera se pueden crear claves DKIM en sistemas donde no se hayan registrado dominios
check_domain = 's'
## Directorio donde se guardaran los archivos de claves para cada dominio 'keys' es el que viene por defecto con openDKIM
keys_dir = 'keys'
## Este es el prefijo con que se asociara la clave con el registro del DNS de nuestro sistema, se puede usar cualquiera
selector = 'mail'
## Para sistemas Centos por ejemplo se requiere indicar la ruta completa de la utilidad dns para subir automáticamente los registros DNS
dns_utility = "/usr/local/psa/bin/dns"
## s = Si, n = No. Define si se desea crear un respaldo de los archivos de claves ya creados
backup = 's'
## Variables generales
domain = ''
erro_logs = list()
domains = list()
## Lista de dominios para la subida por volumen
domains = [
    'domain.com',
]