import socket 
import os

class Paquete_magico():
    def __init__(self,mac):
        self.mac = mac
    def generar(self):
    
        return b'\xff'* 6 + bytes.fromhex(self.mac.replace('-','')) * 16


if __name__ == '__main__':
    puerto = 9
    ip = ''
    mac = ''

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    s.bind((ip,puerto))
    apagado = False

    paquete = Paquete_magico(mac=mac)

    while not apagado:
        msg= s.recv(1024)
        if paquete.generar() == msg:
            os.system('shutdown /s /t 5')
            apagado = True
        