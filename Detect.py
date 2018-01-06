import socket

import struct

import binascii

from datetime import datetime


# Creating raw socket which will capture all the traffic
class snif:

    def __init__(self):
        self.s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))


    def detect(self):
        n = 0
# Dictionary which will be used to record the individual connections and no of requests fron those connections.
        connection = {}

        while True:

            self.frame = self.s.recv(2048)

            if n == 1:

                n = 0

                continue

            n = 1

# Getting informatin about the IP address of the source 

            ds, sr = struct.unpack("!4s4s",self.frame[26:34])

            sp, dp = struct.unpack("!HH",self.frame[34:38])

            sr = socket.inet_ntoa(sr)

            dest_add = socket.inet_ntoa(ds)

            a = self.frame[66:]

            if dp == 80 and 'GET' in a and sp not in connection:

                print("New request to server by IP- {}".format(sr))

                connection.update({sp:1})


            elif dp == 80 and sp in connection:

                count = connection[sp]+1
                if count <10 :
                    connection.update({sp:count})

                    print("fragmented request from connection{}:{}".format(sr, sp))

                    print("  Fragment no {} by this conection".format(count))

                elif count == 10:

                    print("\n\nslow loris attack by {} : port-{} at time- {} \n\n".format(sr,sp,str(datetime.now())[0:19]))

                    with open("warning.log","a") as warning:

                        a = '\n attack conducted by {}:{} at time- {}'.format(sr,sp,str(datetime.now())[0:19])

                        warning.write(a)

                else:
                    print("Attack is in progress by- {}:{}".format(sr,sp))

            if sp==80:

                 bits = struct.unpack("!s",self.frame[47])

                 flags = binascii.hexlify(bits[0])

                 if flags == '11':

                     del(connection[dp])

                 print(connection)
# Initiating the main program to inpect the incoming requests to the apaches server and detect the slow loris atack

if __name__ == "__main__":

    a = snif()

    a.detect()

