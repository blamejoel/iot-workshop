import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# a try/except block is an easy way to prevent the script from crashing in the 
# event that whatever follows the try fails, in this case: if there is no 
# argument passed into our script...
try:
    test = sys.argv[1]          # let's assign our first argument to a shorter 
                                # variable to reference later

    if test == '1':
        GPIO.output(18, 1)      # sets GPIO18 output to HIGH (i.e. True)
        time.sleep(1)           # "sleeps" the python script at this point, for 
                                # 1 second
    else:
        GPIO.output(18, 0)      # sets GPIO18 output to LOW (i.e. False)
except:
    # in case our "try" failed, this except block would run...
    pass    # pass just keeps flow going here

GPIO.cleanup()                  # "cleans up" resources related to GPIO before 
                                # exiting our script

