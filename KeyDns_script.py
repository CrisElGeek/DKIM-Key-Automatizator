#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess, re, shutil, time
from config import selector, base_dir, dns_utility, keys_dir, erro_logs, domains_dir, check_domain

def createKeys(domain_dir, domain):
    os.mkdir(domain_dir, 0755)
    try:
        key_string = "opendkim-genkey -D %s -d %s -s %s" % (domain_dir, domain, selector)
        subprocess.call(key_string, shell=False)
        chown_string = "chown -R opendkim: %s" % domain_dir
        subprocess.call(chown_string, shell=False)
        os.rename(domain_dir + '/' + selector + '.private', domain_dir + '/' + selector)
        keytable_file = open(base_dir + 'KeyTable','a')
        keytable_file.write(selector + "._domainkey." + domain + " " + domain + ":" + selector + ":" + domain_dir + "/" + selector + "\n")
        keytable_file.close()
        signingtable_file = open(base_dir + 'SigningTable','a')
        signingtable_file.write("*@" + domain + " " + selector + "._domainkey." + domain + "\n")
        signingtable_file.close()
        keyText = open(domain_dir + '/' + selector + '.txt', 'r')
        for line in keyText:
            line = line.strip()
            if line.startswith('\"p='):
                l = re.findall("^\".*\"",line)
                break
        keyText.close()
        try:
            l= l[0]
            dns_txt = 'v=DKIM1; k=rsa; ' + l.strip("\"")
            dns_proccess = str(dns_utility + " -a " + domain + " -txt \'" + dns_txt + "\' -domain " + selector + "._domainkey")
            subprocess.call(dns_proccess, shell=False)
            erro_logs.append(str(time.time()) + " - " + domain + " - " + "Clave creada y subida correctamente")
        except subprocess.CalledProcessError as e:
            erro_logs.append(str(time.time()) + " - " + domain + " - " + e.output)
    except IOError, (ErrorNumber, ErrorMessage):
        erro_logs.append(str(time.time()) + " - " + domain + " - " + ErrorMessage)

def directoryManagement(domain, backup):
    def dmCreation():
        domain_dir = base_dir + keys_dir + '/' + domain
        if not os.path.exists(domain_dir):
            if backup == 's':
                try:
                    if not os.path.exists(base_dir + 'opendkim_bk'):
                        os.mkdir(base_dir + 'opendkim_bk', 0755)
                    shutil.copyfile(base_dir + 'KeyTable', base_dir + 'opendkim_bk/KeyTable_' + str(time.time()))
                    shutil.copyfile(base_dir + 'SigningTable', base_dir + 'opendkim_bk/SigningTable_' + str(time.time()))
                except:
                  erro_logs.append(str(time.time()) + " - " + domain + " - Ocurrio un error al momento de crear el respaldo de la configuración actual")
            createKeys(domain_dir, domain)
        else:
            erro_logs.append(str(time.time()) + ' - La clave DKIM  para el dominio ' + domain + ' ya existe. Se omite.')

    domain_exist = 's'
    if not os.path.exists(domains_dir + domain) and check_domain == 's':
        erro_logs.append(str(time.time()) + ' - No se encontro el directorio ' + domains_dir + domain)
        while domain_exist != 'n':
            domain_exist = raw_input('Parece que el dominio ' + domain + ' no existe. ¿Desea agregarlo de todas formas?(s/n):\n> ')
            if domain_exist == 's':
                erro_logs.append(str(time.time()) + " - " + domain + ' - Se procede a crear la clave DKIM aún cuando el dominio parece no existir')
                dmCreation()
                break
            elif domain_exist == 'n':
                erro_logs.append(str(time.time()) + " - " + domain + ' - No se procede a crear la clave DKIM')
                continue
            else:
                print 'Por favor, ingrese una respuesta válida'
    else:
        dmCreation()

## guarda los logs en el archivo predeterminado
def dkim_logs(logs):
    logFile = "dkim.log"
    lf = open(logFile, 'a')
    for log in logs:
        lf.write(log + "\n")
    lf.close()