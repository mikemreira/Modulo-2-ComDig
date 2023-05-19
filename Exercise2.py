import serial

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600)


def main():
    while True:
        if arduino.in_waiting:
            packet = arduino.readlines()
            print(packet)


if __name__ == '__main__':
    main()
