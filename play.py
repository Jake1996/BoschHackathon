import serial
ser = serial.Serial(str(sys.argv[1]),9600)
file_name =  raw_input("Enter File name: ") + ".txt"
n = int(raw_input("Number of repetitions "))
f = open(file_name,'r')
for i in range(0,n):
    for line in f:
        print(line)
        ser.send(line)
    f.seek(0)
f.close()