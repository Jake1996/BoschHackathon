import serial
import sys

file_name = raw_input('enter filename to save into :') + ".txt"
f = open(file_name,'w')
ser = serial.Serial(str(sys.argv[1]),9600)
try:
	read_serial.write('t')
	while True:
		read_serial=ser.readline()
		f.write(read_serial)
		print read_serial
except KeyboardInterrupt:
	read_serial.write('f')
	f.close()