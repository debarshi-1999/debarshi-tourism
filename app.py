
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def login():
    return render_template("anim.html")


if __name__ == "__main__":
    app.run(debug=True)