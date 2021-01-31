from flask import Flask, render_template, url_for, redirect, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "LittleAksMax"
app.permanent_session_lifetime = timedelta(hours=5)

@app.route("/")
def index():
    #if "user" not in session:
    return render_template("index.html")
    #else:
    #    return redirect(url_for("user", usr=session["user"]))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method != "POST":
        return render_template("login.html")

    user = request.form["username"]
    passwd = request.form["password"]
    session["user"] = user # create session

    # TODO: series of checks on entered credentials, make a branch that works on credentials
    return redirect(url_for("user", usr=user))

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method != "POST":
        return render_template("signup.html")
    # TODO: set this up, creating a user, and then joining that session, and redirecting to /<usr>

@app.route("/logout")
def logout():
    session.pop("user", None) # remove data
    return redirect(url_for("index"))

@app.route("/<usr>")
def user(usr):
    if "user" not in session:
        return redirect(url_for("index"))
    else:
        return render_template("user.html", usrname=session["user"])

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
