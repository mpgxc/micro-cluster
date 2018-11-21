from flask import Flask, g, render_template
import sqlite3
import os
from controlers.main import map_network

DATABASE = "./sd.db"

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# check if the database exist, if not create the table and insert a few lines of data
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE node (name TEXT, ip TEXT, function TEXT);")
    conn.commit()
    for l in map_network():
        cur.execute("INSERT INTO node VALUES(l);")
        conn.commit()
    conn.close()


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db().cursor()
    res = cur.execute("select * from node")
    return render_template("worker.html", node=res)
    return render_template('worker.html',  nodes=map_network())


if __name__ == "__main__":
    """
	Use python sqlite3 to create a local database, insert some basic data and then
	display the data using the flask templating.
	
	http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
    """
    app.run()