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
import sys

from master import main
import os

app = Flask(__name__)


def make_connection():

    url = os.environ.get(
        'CLOUDAMQP_URL', 'amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'
    )

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='master')

    def callback(ch, method, properties, body):

        Saida = open('data.txt', 'w')
        Saida.write(str(body.decode()))
        Saida.close()

    channel.basic_consume(callback, queue='master', no_ack=True)
    channel.start_consuming()

    channel.stop_consuming()
    connection.close()


'''
def make_connection():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'))
    channel = connection.channel()
    channel.queue_declare(queue='master')

    def callback(ch, method, properties, body):
        print(" [x] Recebido %r" % body)

        Saida = open('data.txt', 'w')
        Saida.write(str(body.decode()))
        Saida.close()

    channel.basic_consume(callback, queue='master', no_ack=True)
    channel.start_consuming()
'''


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

    return render_template('index.html')


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


@app.route('/worker')
def update():
    time.sleep(1.2)
    return render_template('worker.html',  nodes=map_network())


if __name__ == '__main__':

    QUANTED = sys.argv[1]
    
    sk = open("cache/quant.txt", "w")
    sk.write(QUANTED)
    sk.close()

    app.run(host='127.0.0.1', port=45259, debug=True)
