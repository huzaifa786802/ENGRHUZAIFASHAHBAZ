import serial
import time

# Define serial communication parameters
arduino_port = "COM6"  # Replace with the COM port of your Arduino Uno
baud_rate = 9600       # Must match the baud rate in the Arduino sketch
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the serial connection to initialize

def send_command(command):
    ser.write(command.encode())  # Send the command to Arduino
    print(f"Sent command: {command}")
    time.sleep(0.5)  # Wait for the Arduino to process the command

try:
    while True:
        for i in range(8):  # Turn on LEDs one by one
            send_command(f"ON:{i}\n")
        for i in range(8):  # Turn off LEDs one by one
            send_command(f"OFF:{i}\n")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
