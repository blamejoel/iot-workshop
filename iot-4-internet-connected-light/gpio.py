import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    test = sys.argv[1]

    if test == '1':
        GPIO.output(18, 1)
        time.sleep(1)
    else:
        GPIO.output(18, 0)
except:
    pass

GPIO.cleanup()

