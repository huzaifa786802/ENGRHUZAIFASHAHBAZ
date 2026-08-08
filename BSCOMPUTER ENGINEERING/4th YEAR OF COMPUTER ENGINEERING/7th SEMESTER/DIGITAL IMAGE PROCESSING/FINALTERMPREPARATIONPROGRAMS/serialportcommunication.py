import serial
import time
import serial.tools.list_ports as ports
# List available COM ports (optional for troubleshooting)
com_ports = list(ports.comports())
print("Available COM Ports:")
for i in com_ports:
    print(i.device)

# Set up the serial connection
try:
    ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port if needed
    time.sleep(2)  # Wait for the connection to stabilize
    print("Connected to COM3")
except serial.SerialException:
    print("Error: Could not open COM3")
    exit()
print("Press 'H' to turn LED ON and 'L' to turn LED OFF.\n")
# Communication loop
try:
    for i in range(10):  # Adjust the range for the number of inputs you want to allow
        key = input("Enter command (H/L): ").strip().upper()  # Ensure clean input
        if key in ['H', 'L']:
            ser.write(key.encode())  # Send the command to the microcontroller
            print(f"Sent: {key}")
        else:
            print("Invalid command. Please press 'H' or 'L'.")
        time.sleep(1)  # Delay for stability
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
# Close the serial connection
ser.close()
print("Serial connection closed.")