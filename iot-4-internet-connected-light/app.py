from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
app.debug=True

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route('/')
def index():
    return 'Try http://localhost:5000/on!'

@app.route('/on')
def led_on():
    GPIO.output(18, 1)
    return 'LED on!'

@app.route('/off')
def led_off():
    GPIO.output(18, 0)
    return 'LED off!'

if __name__ == "__main__":
    app.run()

