from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!\n"


@app.route("/goodbye/<name>")
def goodbye(name):
    return f'Goodbye, {escape(name).title()}!'


@app.route("/ping")
def pingpong():
    return "pong!\n"


if __name__ == "__main__":
    app.run(debug=False)
