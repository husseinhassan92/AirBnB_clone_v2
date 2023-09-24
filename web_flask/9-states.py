#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: display "Hello HBNB!"
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """display text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display custom text given"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display custom text given"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display custom text given"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_html(n):
    """display custom text given"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_odd(n):
    """display custom text given"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.teardown_appcontext
def treardown(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """"Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name."""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """"Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name."""
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """"Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name."""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
