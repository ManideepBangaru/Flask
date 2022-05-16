from flask import Flask, flash, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField
from wtforms.validators import DataRequired
# from flask_sqlalchemy import SQLAlchemy
# from functools import update_wrapper
# from pkg_resources import safe_extra
# from turtle import st
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "AdMiN1234"
)
my_cursor = mydb.cursor()

# create a flask instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "my super secret key"

# Add Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:AdMiN1234@localhost/teamalpha"

class NamerForm(FlaskForm):
    name = StringField("Enter your Name : ", validators=[DataRequired()])
    age = IntegerRangeField("Enter your Age : ", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create a route decorator
# @app.route('/')

# def index():
#     return "<h1> Hello World </h1>"

# safe
# capitalize
# upper
# lower
# title
# striptags

# def index():
#     my_name = "Manideep"
#     stuff = "<p> This is a <strong> bold </strong> text </p>"
#     favoritePizza = ["pepperoni","cheeseburst","barbecue",99]
#     return render_template("home.html",
#     first_name = my_name,
#     stuff=stuff,
#     favoritePizza = favoritePizza)

# /localhost:5000/user/manideep
# @app.route('/user/<name>')
# def user(name):
#     return render_template("user.html",user_name=name)

@app.route("/", methods = ["GET", "POST"])
def takeIP():
    name = None
    age = None
    form = NamerForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        print(name)
        print(age)

        my_cursor.execute("INSERT INTO teamalpha.teamalph_a VALUES (%s,%s);",(name,age))
        mydb.commit()

        form.name.data = ""
        form.age.data = ""
    return render_template("takeInput.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)