from flask import Flask, render_template, request
import requests
from controlers.main import map_network
import pika

from threading import Thread
import threading
import multiprocessing
import subprocess
import time


from master import main


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


@app.route('/')
def index():

    task_connection()  # Aguarda requisição do Cliente
    # makeDoubleTask()

    # main()  # inicia o Master

    return render_template('index.html')


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


@app.route('/worker')
def update():
    return render_template('worker.html',  nodes=map_network())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8070, debug=True)
