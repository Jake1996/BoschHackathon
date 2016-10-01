#!/usr/bin/python
import socket
import time
import sys
s = socket.socket()
s.connect((str(sys.argv[0]), str(sys[argv[1])))
while True:
    data=raw_input()
    s.send(data.encode('utf-8'))
time.sleep(3)
s.close()
