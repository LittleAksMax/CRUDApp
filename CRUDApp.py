from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", stylesheet=False)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #user = request.form["username"]
        print(request.data)
        return redirect(url_for("user", usr="asdf"))
    else:
        return render_template("login.html", stylesheet=True)

@app.route("/join")
def join():
    return render_template("signup.html", stylesheet=True)

@app.route("/<usr>")
def user(usr, stylesheet=True):
    return render_template("user.html")

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
