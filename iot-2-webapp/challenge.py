from flask import Flask, render_template

app = Flask(__name__)
app.debug=True

# let's define a global variable temps, which is a list
temps = []

@app.route('/<temp>')
def index(temp):
    # ghetto check to make sure that temp exists
    if temp:
        temps.append(temp)  # add the temp to the end of our temps list

    # lastly, let's render our template page, and give it the list of temps
    return render_template('challenge.html', temps=temps)

if __name__ == "__main__":
    app.run()
