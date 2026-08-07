import serial
import time
import serial.tools.list_ports as ports

# com_ports = list(ports.comports())  # create a list of com ['COM1','COM2']
# for i in com_ports:
#     print(i.device) 

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
print("Press H to turn LED ON and Press L to turn LED OFF\n")
for i in range(10):
    key = input()
    ser.write(key.encode())   # send a byte
    time.sleep(1)        # wait 1 seconds
ser.close()