import serial

# Replace with the actual serial port and baud rate
serial_port = "/dev/ttyUSB0"  # Example serial port for Linux
baud_rate = 9600  # Example baud rate

try:
    # Create a serial object
    ser = serial.Serial(port=serial_port, baudrate=baud_rate, timeout=1)

    # Open the serial port
    ser.open()

    if ser.is_open:
        print(f"Serial port {serial_port} opened successfully.")
        
        # Data to send to the serial device
        data_to_send = "Hello, serial device!"

        # Write data to the serial port
        ser.write(data_to_send.encode())

        # Read the response from the serial device
        response = ser.read(100)  # Read up to 100 bytes
        print(f"Received response from serial device: {response.decode()}")

    else:
        print(f"Failed to open serial port {serial_port}.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the serial port
    if ser.is_open:
        ser.close()
        print(f"Serial port {serial_port} closed.")
