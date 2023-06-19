import serial
import time
import FletcherChecksumLib as fletcher

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=3)

'''
# 2) a)
while 1:
    time.sleep(3)
    receivedStr = arduino.readline().rstrip().decode('utf-8')
    print(receivedStr)
    '''

# 2) b)
'''
while 1:
    time.sleep(10)
    receivedStr, fletcher_sum = arduino.readline().rstrip().decode().split(",")
    my_sum = fletcher.FletcherChecksumStr.get_fletcher16(str(int(receivedStr) ^ 0x01))['Fletcher16_dec']
    print("Fletcher calculated in Python = ", my_sum)
    print("Fletcher received from Arduino = ", fletcher_sum)
    if int(my_sum) == int(fletcher_sum):
        print("Success no errors")
    else:
        print("Errors")
'''


# 2) c)
while 1:
    time.sleep(10)
    receivedStr, fletcher_sum = arduino.readline().rstrip().decode().split(",")
    print("RECEIVED", receivedStr)
    mutatedStr = str(receivedStr).replace("739", "658")
    print("MUTATED", mutatedStr)
    my_sum = fletcher.FletcherChecksumStr.get_fletcher16(mutatedStr)['Fletcher16_dec']
    print(my_sum)
    print("FLETCHER", fletcher_sum)
    if int(my_sum) == int(fletcher_sum):
        print("SUCCESS NO ERRORS")
    else:
        print("Errors")

