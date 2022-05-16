from flask import Flask, render_template

# create a flask instance

app = Flask(__name__)


# create a route decorator

@app.route('/')

def index():
    return "<h1> Hello World </h1>"

# /localhost:5000/user/manideep
@app.route('/user/<name>')
def index():
    return "<h1> Hello </h1>"
