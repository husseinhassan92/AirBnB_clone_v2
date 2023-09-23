#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
"""

from flask import flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display text"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
