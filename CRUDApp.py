from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", stylesheet=False)

@app.route("/login")
def login():
    return render_template("login.html", stylesheet=True)

@app.route("/join")
def join():
    return render_template("signup.html", stylesheet=True)

@app.route("/<usr>")
def user(usr, stylesheet=True):
    return ""

@app.route("/<usr>/insert")
def insert():
    return render_template("insert.html", stylesheet=True)

@app.route("/<usr>/update")
def update():
    return render_template("update.html", stylesheet=True)

@app.route("/<usr>/delete")
def delete():
    return render_template("delete.html", stylesheet=True)

if __name__ == "__main__":
    app.run(debug=True)
