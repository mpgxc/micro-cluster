import pika
from read_load import load
import os


'''
def send(file):

    connection = pika.BlockingConnection( pika.ConnectionParameters())
    channel = connection.channel()
    channel.queue_declare(queue='master')
    channel.basic_publish(exchange='', routing_key='master', body = file)
    connection.close()
'''
# ----------------------------------------------------


def send(file):

    url = os.environ.get(
        'CLOUDAMQP_URL', 'amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'
    )

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue="master")  # Declare a queue
    channel.basic_publish(exchange='', routing_key="master", body=file)
    connection.close()

# ---------------------------------------------------------------


'''
def receive():

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'))
    channel = connection.channel()
    channel.queue_declare(queue='cliente')

    def callback(ch, method, properties, body):
        print(" [x] Recebido Cliente %r" % body)

        Saida = open('data.txt', 'w')
        Saida.write(str(body.decode()))
        Saida.close()

    channel.basic_consume(callback, queue='cliente', no_ack=True)
    channel.start_consuming()

    channel.stop_consuming()
    connection.close()
'''


def receive():

    url = os.environ.get(
        'CLOUDAMQP_URL', 'amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'
    )

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='cliente')

    def callback(ch, method, properties, body):

        Saida = open('data.txt', 'w')
        Saida.write(str(body.decode()))
        Saida.close()

    channel.basic_consume(callback, queue='cliente', no_ack=True)
    channel.start_consuming()

    channel.stop_consuming()
    connection.close()
