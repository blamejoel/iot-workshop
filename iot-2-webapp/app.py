# Import the "Flask" and "render_template" functions from the module "flask"
from flask import Flask, render_template

# instantiate a new Flask object.
# __name__ is a keyword in Python, that references the current module
# ¯\_(ツ)_/¯
app = Flask(__name__)
app.debug=True          # this tells Flask to start up in debug mode

@app.route('/')         # Flask will use route decorators like this to find 
                        # instructions for what to do when a user visits a 
                        # specific resource, in this case the "root" i.e. just 
                        # http://localhost/ <-- see that slash?

def index():            # Flask will execute whatever function is defined 
                        # after a decorator when that route is requested

    # stuff you want to happen would normally go here...
    # maybe you want to increment a counter, maybe you want to run some 
    # random script...
    return render_template('test.html') # here we're just telling Flask to 
                                        # return the rendered template based 
                                        # off of our "test.html" page

# a different route...
@app.route('/new')
def new():
    return render_template('new.html')

# a route with variables...
@app.route('/<var>')
def var(var):   # in the slides, this is index(var), we've renamed it because 
                # there's already an index() defined above...

    # print the variable to the console so we can have some 
    # instant feedback on the console
    print('The variable passed in is: {}'.format(var))  

    # in the below line, Flask will look for {{msg}} in the template 
    # test2.html and replace it with the variable "var"
    return render_template('test2.html', msg=var)

# this last bit just tells flask to check if this script is the "main" script 
# is the main script beig run and not just being imported in as a module to 
# another script. Think of this of a void main() {} in C/C++
if __name__ == "__main__":
    app.run()   # app is a Flask object remember? run() is a function of a 
                # Flask object that will start the Flask server
