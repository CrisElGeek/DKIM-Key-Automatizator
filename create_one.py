#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import domain, backup, erro_logs
from KeyDns_script import directoryManagement, dkim_logs

while domain != "quit":
    domain = raw_input("Por favor ingrese el dominio: (Salir: quit)\n> ")
    if domain == "quit":
        continue
    elif len(domain) >= 6:
        resp = 's'
        while resp != "n":
            resp = raw_input("Esta seguro que desea integrar DKIM con el dominio %s (s/n)\n> " % domain)
            if resp == "n":
                continue
            elif resp == "s":
                while backup:
                    backup = raw_input("Desea realizar un respaldo de la configuración atual (s/n)\n> ")
                    if backup == 'n' or backup == 's':
                        directoryManagement(domain, backup)
                        dkim_logs(erro_logs)
                        erro_logs = []
                        break
                    else:
                        print "No entendi su respuesta"
                break
            else:
                print "No entiendo su respuesta"
                continue
    elif len(domain) < 6 or len(domain) >= 1:
        print "El dominio debe contener al menos 6 caracteres"
        continue

print "Programa finalizado"