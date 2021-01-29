from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/join")
def join():
    return render_template("signup.html")

@app.route("/<usr>")
def user(usr):
    return ""

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
    app.run()
