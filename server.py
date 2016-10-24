#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dict = {}

    def handle(self):
        IP = self.client_address[0]
        print('IP: ' + IP)
        PORT = self.client_address[1]
        print('PORT: ' + str(PORT))

        line = self.rfile.read()
        LINE = line.decode('utf-8')
        print("El cliente nos manda " + LINE)

        if LINE.split(' ')[0] == "REGISTER":
            Expires = LINE.split(' ')[2]
            time_expires = time.gmtime(int(Expires))
            SIP = LINE.split(' ')[1]
            print('REGISTER ' + SIP + ' ' + LINE.split(' ')[3])
            print('Expires: ' + Expires)
            DIRECTION = SIP.split(':')[1]
            print('Direction: ' + DIRECTION)
            self.dict[DIRECTION] = IP
#            for direcciones in self.dict :
#               print(direcciones)
#               print(IP)
            if Expires == "0":
                if DIRECTION in self.dict:
                    del self.dict[DIRECTION]
                    print(LINE.split(' ')[3] + '200 OK' + '\r\n\r\n')
                else:
                    print("USUARIO NO ENCONTRADO")
            if time_expires == "0":
                del self.dict[DIRECTION]

            print(self.dict)

        self.wfile.write(b' SIP/2.0 200 OK\r\n\r\n')

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
