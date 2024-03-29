#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print("Status: ", data.decode(encoding="utf-8"))
        except Exception:
            print('Exit...')
            break


print('Tello Cli.')
print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')
print('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True:

    try:
        msg = input("");

        if not msg:
            break

        if 'end' in msg:
            print ('...')
            sock.close()
            break

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
