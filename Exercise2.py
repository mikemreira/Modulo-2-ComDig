import serial
import array
import time
import FletcherChecksumLib as fletcher

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=3)


def geometric_progression(n, u, r):
    arr = array.array("f", (0 for _ in range(0, n)))
    for i in range(0, n):
        arr[i] = (u * r) ** i
    return arr


while 1:
    time.sleep(3)
    receivedStr = arduino.readline()  # .rstrip().decode("utf-8")
    print(fletcher.FletcherChecksumBytes.get_fletcher32(receivedStr))

