import numpy as np
import struct
import socket
import time

sock = socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM)

UDP_IP = "127.0.0.1" #Target IP Address
UDP_PORT_TX = 8000
UDP_PORT_RX = 8001

sock.bind((UDP_IP, UDP_PORT_RX))
recvData = None

while True:
    x = round(np.random.uniform(-0.5,0.5),2)
    y = round(np.random.uniform(-0.1,0.1),2)
    z = round(np.random.uniform(-0.5,0.5),2)
    sendMessage = struct.pack('fff', x, y, z)# Send this string to other application
    sock.sendto(sendMessage, (UDP_IP, UDP_PORT_TX))  
    

    try:
        recvData, addr = sock.recvfrom(1024)
    except:
        time.sleep(1)

    if recvData != None: # if NEW data has been received since last ReadReceivedData function call
        pose = struct.unpack('fff', recvData)
        print(pose[0], pose[1], pose[2]) # print new received data
    time.sleep(1)