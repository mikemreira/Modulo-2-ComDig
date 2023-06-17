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
    receivedStr, fletcher_sum = arduino.readline().rstrip().decode().split(",")
    print(receivedStr)
    my_sum = fletcher.FletcherChecksumStr.get_fletcher16(str(int(receivedStr) + 1))['Fletcher16_dec']
    print(my_sum)
    print("FLETCHER", fletcher_sum)
    if int(my_sum) == int(fletcher_sum):
        print("SUCCESS NO ERRORS")
    else:
        print("Errors")

