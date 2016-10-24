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

METODO = sys.argv[3].upper()
USUARIO= sys.argv[4]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket: #(red, paquete)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT)) #Tupla (multiples valores que no se pueden modificar)
if sys.argv[3] == 'REGISTER':
    REGISTER  = ('REGISTER' + ' sip: ' + sys.argv[4] + ' SIP/2.0')
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n\r\n')
try:
    data = my_socket.recv(1024)
except ConnectionRefusedError:
    sys.exit("Connection refused")
    
print('Recibido -- ', data.decode('utf-8'))  #Decode: Pasar de bytes a utf8

my_socket.close()
print('fin')
