from flask import Flask, render_template, request, g, redirect, url_for
import requests
from controlers.main import map_network
import pika
import subprocess
from threading import Thread
import threading
import multiprocessing
import subprocess
import time
import sys
import sqlite3
from call_nodes import connectNodes
import os
from count_nodes import make_count
from master import main
from forms import Entrada
import os
from sender import server_Recebe

DATABASE = "./database.db"


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'


if not os.path.exists(DATABASE):

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE users (id integer primary key autoincrement, name TEXT not null, ip TEXT not null, ram TEXT not null, cores TEXT not null);"
    )

    conn.commit()
    conn.close()


def insert_values(name, ip, ram, cores):

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, ip, ram, cores) VALUES('"+str(name)+"', '" +
        str(ip)+"', '"+str(ram)+"', '"+str(cores)+"');"
    )

    conn.commit()
    conn.close()


def remove_values(name):

    conn = sqlite3.connect(DATABASE)
    sql = "delete from users where name=?"

    cur = conn.cursor()
    try:
        cur.execute(sql, (name,))
    except:
        pass

    conn.commit()
    conn.close()


def get_dbase():

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# ---------------------------------------------------


def task_connection():
    tasK = threading.Thread(name="t1", target=makeDoubleTask)
    tasK.start()


def makeDoubleTask():

    pPal = multiprocessing.Process(target=server_Recebe)
    pCor = multiprocessing.Process(target=main)

    pCor.start()
    pPal.start()

    pCor.join()
    pPal.join()
# ------------------

# Paginas


@app.route('/')
def index():

    task_connection()  # Aguarda requisição do Cliente

    connectNodes()

    qtd = make_count()

    return render_template('index.html', qtd=qtd)


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')


@app.route('/add', methods=['GET', 'POST'])
def adiciona():

    campos = Entrada(request.form)
    if campos.name.data != "" or campos.ip.data != "" or campos.ram.data != "" or campos.cores.data != "":
        insert_values(campos.name.data, campos.ip.data,
                      campos.ram.data, campos.cores.data)
        return redirect(url_for('sucesso'))

    return render_template('cadastro.html', campos=campos)


@app.route('/rem', methods=['GET', 'POST'])
def remove():
    campos = Entrada(request.form)
    if campos.name.data != "":
        remove_values(campos.name.data)
        return redirect(url_for('sucesso'))

    return render_template('remover.html', campos=campos)


@app.route('/worker')
def update():

    cur = get_dbase().cursor()
    res = cur.execute("select * from users")

    time.sleep(1)

    return render_template('worker.html',  nodes=res)  # map_network()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=47258, debug=True)