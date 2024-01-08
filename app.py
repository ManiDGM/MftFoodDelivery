from flask import Flask, render_template, redirect, request, session

from controller import *
from flask_session import Session

app = Flask(__name__, template_folder="view", static_folder="view/static")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_PERMANENT"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("/login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        data = CustomerController.login(email, password)



@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        status, data = CustomerController.save(
            request.form.get("first_name"),
            request.form.get("last_name"),
            request.form.get("email"),
            request.form.get("password"))

    return render_template("signup.html")



@app.route("/forget")
def forget():
    return render_template("forget-password.html")


app.run()