#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        IP = self.client_address[0]
        print('IP: ' + IP)
        PORT = self.client_address[1]
        print('PORT: ' + str(PORT))

        self.wfile.write(b"Hemos recibido tu peticion")  #wfile: Enviar por la red (en udp)
        for line in self.rfile:    #rfile: Leer fichero
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), EchoHandler)    #Dos parametros, tupla (IP y Puerto) y manejador (echohandler: trata las peticiones)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
