#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket      #lo utilizamos para abrir caminos del cliente al servidor

# Constantes. Dirección IP del servidor y contenido a enviar -(En mayúsculas)

SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE = sys.argv[3:]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket: #(red, paquete)
    my_socket.connect((SERVER, PORT)) #Tupla (multiples valores que no se pueden modificar)
    print("Enviando:", ' '.join(LINE))
    my_socket.send(bytes(' '.join(LINE), 'utf-8') + b'\r\n')   #b: bytes
    data = my_socket.recv(1024)    #1024: tamaño del bufer en bytes
    print('Recibido -- ', data.decode('utf-8'))  #Decode: Pasar de bytes a utf8

print("Socket terminado.")
