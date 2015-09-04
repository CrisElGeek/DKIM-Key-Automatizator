#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import domains, backup, erro_logs
from KeyDns_script import directoryManagement, dkim_logs

for item in domains:
    directoryManagement(item,backup)
dkim_logs(erro_logs)