from flask import Flask, render_template
import RPi.GPIO as GPIO     # imports the appropriate module for GPIO control

app = Flask(__name__)
app.debug=True

GPIO.setmode(GPIO.BCM)      # sets the GPIO pin numbering scheme, in this case, 
                            # we're using the broadcom GPIO numbering, i.e. 
                            # 18 will mean GPIO18 (physical pin 12)

GPIO.setup(18, GPIO.OUT)    # sets GPIO18 as an output

@app.route('/')
def index():
    return 'Try http://localhost:5000/on!'  # returns a gentle reminder on how 
                                            # to use our simple GPIO webapp

@app.route('/on')
def led_on():
    GPIO.output(18, 1)                      # sets GPIO18, to HIGH (True, etc.)
    return 'LED on!'

@app.route('/off')
def led_off():
    GPIO.output(18, 0)                      # sets GPIO18, to LOW (False, etc.)
    return 'LED off!'

if __name__ == "__main__":
    app.run()

