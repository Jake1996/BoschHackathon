import socket
import sys
import time
ser = socket.socket()
ser.connect((str(sys.argv[1]), int(sys.argv[2])))
file_name =  raw_input("Enter File name: ") + ".txt"
n = int(raw_input("Number of repetitions "))
f = open(file_name,'r')
for i in range(0,n):
    for line in f:
        print(line)
        time.sleep(1)
        ser.send(line.encode('utf-8'))
    f.seek(0)
f.close()
s.close()