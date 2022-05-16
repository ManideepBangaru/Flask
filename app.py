from flask import Flask, render_template

# create a flask instance 

app = Flask(__name__)


# create a route decorator

@app.route('/')

def index():
    return "<h1> Hello World, This is Manideep Bangaru </h1>"