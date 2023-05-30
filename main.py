from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculations")
def calculate():
    return render_template("calculations.html")


@app.route("/names")
def home():
    names = ["Jonas", "Antanas", "Petras"]
    return render_template("names.html", my_list=names)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
