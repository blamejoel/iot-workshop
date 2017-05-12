import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)  # sets a reference to GPIO PWM pin 18, at 50Hz

try:
    test = sys.argv[1]

    pwm.start(int(test))     # starts PWM with duty cycle equal to var
    time.sleep(1)

except:
    pass

GPIO.cleanup()

