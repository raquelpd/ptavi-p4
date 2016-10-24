#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket      #lo utilizamos para abrir caminos del cliente al servidor

# Constantes. Dirección IP del servidor y contenido a enviar -(En mayúsculas)

SERVER = sys.argv[1]
try:
    PORT = int(sys.argv[2])
except ValueError:
    sys.exit("invalid Port")
LINE = ' '.join(sys.argv[4:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT)) #Tupla (multiples valores que no se pueden modificar)
if sys.argv[3] == 'REGISTER':
    REGISTER  = ('REGISTER' + ' sip:' + ' '.join(sys.argv[4:]) + ' SIP/2.0')
    print('enviando' + LINE)
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n\r\n')
    data = my_socket.recv(1024)
    
print( 'Recibido -- ', data.decode('utf-8'))  #Decode: Pasar de bytes a utf8

print('fin')
