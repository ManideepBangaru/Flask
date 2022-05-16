from functools import update_wrapper
from flask import Flask, render_template
from pkg_resources import safe_extra

# create a flask instance
app = Flask(__name__)


# create a route decorator
@app.route('/')

# def index():
#     return "<h1> Hello World </h1>"

# safe
# capitalize
# upper
# lower
# title
# striptags

def index():
    my_name = "Manideep"
    stuff = "<p> This is a <strong> bold </strong> text </p>"
    favoritePizza = ["pepperoni","cheeseburst","barbecue",99]
    return render_template("home.html",
    first_name = my_name,
    stuff=stuff,
    favoritePizza = favoritePizza)

# /localhost:5000/user/manideep
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

if __name__ == "__main__":
    app.run(debug=True)