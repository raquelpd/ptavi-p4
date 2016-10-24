#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar -(En mayúsculas)

try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    REGISTER = sys.argv[3]
    DIRECCION = sys.argv[4]
    TIME = sys.argv[5]

except IndexError:
    sys.exit('Usage: client.py ip puerto register sip_address expires_value')


SERVER = sys.argv[1]
try:
    PORT = int(sys.argv[2])
except ValueError:
    sys.exit("invalid Port")
LINE = ' '.join(sys.argv[3:])

DIRECTION = sys.argv[4]
Expires = sys.argv[5]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

if sys.argv[3] == 'REGISTER':
    TIME = ('Expires: ' + Expires + '\r\n\r\n')
    REGISTER = ('REGISTER' + ' sip:' + ' '.join(sys.argv[4:]) + ' SIP/2.0')
    print('enviando' + LINE)
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n\r\n' + bytes(TIME, 'utf-8'))
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))

print('fin')
