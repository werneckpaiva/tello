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
sock_command = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

sock_command.bind(locaddr)

def recv_status():
    while True:
        data, server = sock_command.recvfrom(1518)
        status = data.decode(encoding="utf-8")
        if status:
            return status

def send_unsafe_command(cmd):
    msg = cmd.encode(encoding="utf-8")
    sent = sock_command.sendto(msg, tello_address)
# recvThread = threading.Thread(target=recv_status)
# recvThread.start()

def send_command(cmd):
    send_unsafe_command(cmd)
    status = recv_status()
    return status


print('Tello Ballet')

# command takeoff land flip forward back left right up down cw ccw speed speed?
cmds = ["command", "takeoff", "up 20", "left 20", "forward 100", "back 100", "cw 360", "land"]
for cmd in cmds:
    try:
        # Send data
        print("Sending: %s" % cmd)
        for i in range(5):
            status = send_command(cmd)
            if status == "ok":
                break
    except KeyboardInterrupt:
        break
print ('Ending...')
send_unsafe_command("emergency")
send_unsafe_command("end")
sock.close()
