#!/usr/bin/python
#first argument is interface second argument is port
import socket
import time
import sys
#import serial
#ser = serial.Serial(str(sys.argv[0]),9600)
s = socket.socket()
s.bind(('', int(sys.argv[1])))
s.listen(5)
c, addr = s.accept() #use c from here on c is controller
while True:
    toRun = c.recv(1024)
#    ser.send(toRun)
    print toRun
s.close()
