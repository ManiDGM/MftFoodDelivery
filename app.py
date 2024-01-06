from flask import Flask, render_template, redirect, request, session

from controller import *
from flask_session import Session

app = Flask(__name__, template_folder="view", static_folder="view/assets")
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


app.run()