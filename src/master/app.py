from flask import Flask, render_template, request
import requests
from controlers.main import map_network
import pika
import subprocess
from threading import Thread
import threading
import multiprocessing
import subprocess
import time
from flask import Flask, g, render_template
import sqlite3
import os

from master import main

DATABASE = "./sd.db"

app = Flask(__name__)


def make_connection():

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='master')

    def callback(ch, method, properties, body):
        print(" [x] Recebido %r" % body)

        Saida = open('data.txt', 'w')
        Saida.write(str(body.decode()))

    channel.basic_consume(callback, queue='master', no_ack=True)
    channel.start_consuming()


def task_connection():

    tasK = threading.Thread(name="t1", target=makeDoubleTask)
    tasK.start()


def makeDoubleTask():

    pPal = multiprocessing.Process(target=make_connection)
    pCor = multiprocessing.Process(target=main)

    pCor.start()
    pPal.start()

    pCor.join()
    pPal.join()

def makeCreate():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("CREATE TABLE node (name TEXT, ip TEXT, function TEXT);")
        conn.commit()

        conn.close()


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


@app.route('/')
def index():

    task_connection()  # Aguarda requisição do Cliente

    return render_template('index.html')
  
def makeInsert():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.executemany(""" INSERT INTO node (name, ip, function) VALUES (?,?,?)""", (name, ip, function))
    conn.commit()

@app.route('/add', methods=['POST', 'GET'])   
def insere():   
    """if request.method=='POST':
        nome = request.form['nome']
        ip = request.form['ip']
        fun = request.form['so']
        dbHandler.makeInsert(nome, ip, so)
        node = dbHandler.retrieveUsers()
        return render_template('cadastro.html', node = res)
    else:"""
    return render_template('cadastro.html')


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


@app.route('/worker')
def update():
    cur = get_db().cursor()
    res = cur.execute("select * from node")
    return render_template("worker.html", node=res)

@app.route('/delete', methods=['POST'])
def delete_entry():
    conn = sqlite3.connect(DATABASE)
    cur = get_db().cursor()
    res = cur.execute('DELETE FROM node WHERE ip = ''' +  request.args.get("ip")+ '"')
    res = cur.fetchall()
    conn.commit()
    flash('Entry deleted')
    return render_template('remocao.html', node=res)

if __name__ == '__main__':
    ids = [1,2,3,4,5]
    time.sleep(3)
    return render_template('worker.html', nodes = ids)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2520, debug=True)
