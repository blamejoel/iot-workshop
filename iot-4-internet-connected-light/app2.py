from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
app.debug=True

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)  # sets a reference to GPIO PWM pin 18, at 50Hz

@app.route('/')
def index():
    return 'Try http://localhost:5000/on!'

@app.route('/on')
def led_on():
    pwm.stop()              # stops PWM if it's active, why not?
    GPIO.output(18, 1)
    return 'LED on!'

@app.route('/off')
def led_off():
    pwm.stop()              # stops PWM if it's active, why not?
    GPIO.output(18, 0)
    return 'LED off!'

@app.route('/pwm/<var>')
def var(var):
    pwm.stop()              # stops PWM if it's active, why not?
    pwm.start(int(var))     # starts PWM with duty cycle equal to var
    # note, we could also use pwm.ChangeDutyCycle(var) instead of stopping and 
    # starting the PWM pin
    return 'PWM duty cycle set to {}'.format(var)

if __name__ == "__main__":
    app.run()
