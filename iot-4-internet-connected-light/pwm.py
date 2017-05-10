import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)

try:
    test = sys.argv[1]

    pwm.start(int(test))
    time.sleep(1)

except:
    pass

GPIO.cleanup()

