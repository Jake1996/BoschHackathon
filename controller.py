#!/usr/bin/python
import socket
import time
import sys
s = socket.socket()
s.connect((str(sys.argv[1]), int(sys.argv[2])))
while True:
    data=raw_input()
    s.send(data.encode('utf-8'))
s.close()
