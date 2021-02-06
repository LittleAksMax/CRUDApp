from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
import database_handler

app = Flask(__name__)
app.secret_key = "LittleAksMax"
app.permanent_session_lifetime = timedelta(hours=5)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method != "POST":
        return render_template("login.html")

    invalid = False
    user = request.form["username"]
    passwd = request.form["password"]

    if user == "" or passwd == "":
        flash("Must fill in all boxes", "error")
        invalid = True

    if not invalid and not database_handler.check_username_already_used(user):
        flash("These details haven't been registered, did you mean to sign up instead?", "error")
        invalid = True
    if not invalid and not database_handler.check_password(user, passwd):
        flash("Incorrect password", "error")
        invalid = True

    if not invalid:
        session["user"] = user # create session
        session["id"] = database_handler.get_user_id(user)
        session["emps"] = database_handler.get_employees(session["id"])
        return redirect(url_for("user", usr=user))
    else:
        return redirect(url_for("login"))

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method != "POST":
        return render_template("signup.html")

    user = request.form["username"]
    passwd = request.form["password"]
    email = request.form["email"]

    invalid = False
    if user == "" or passwd == "" or email == "":
        flash("Must fill in all boxes", "error")
        invalid = True
    if database_handler.check_username_already_used(user):
        flash("This username has already been used!", "error")
        invalid = True
    if database_handler.check_email_already_used(email):
        flash("This email has already been used!", "error")
        invalid = True

    if not invalid:
        # add to database
        database_handler.insert_user(user, passwd, email)

        session["user"] = user # create session
        session["id"] = database_handler.get_user_id(user)
        return redirect(url_for("user", usr=user, employees=database_handler.get_employees(session["id"])))
    else:
        return redirect(url_for("join"))

@app.route("/logout")
def logout():
    flash("Login successful")
    session.pop("user", None) # remove data
    return redirect(url_for("index"))

@app.route("/<usr>")
def user(usr):
    if "user" not in session:
        return redirect(url_for("index"))
    else:
        flash("Authentication successful")
        return render_template("user.html", usrname=usr, employees=session["emps"])

@app.route("/<usr>/insert")
def insert():
    return render_template("insert.html")

@app.route("/<usr>/update")
def update():
    return render_template("update.html")

@app.route("/<usr>/delete")
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    app.run(debug=True)
