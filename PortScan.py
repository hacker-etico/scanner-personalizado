#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear', shell=True)
remoteServer    = raw_input("Digite o ip ou host: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
print "Aguarde terminar de scanear do ip", remoteServerIP
t1 = datetime.now()
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Porta {}:   aberta".format(port)
        sock.close()
except KeyboardInterrupt:
    print "preciona a tecla Ctrl+C"
    sys.exit()
except socket.gaierror:
    print 'Hostname deveria esta com erro. sair'
    sys.exit()
except socket.error:
    print "nao conetar ao server"
    sys.exit()

t2 = datetime.now()
total =  t2 - t1
print 'Scanning comleto: ', total
