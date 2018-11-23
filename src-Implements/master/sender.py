import pika
import os


def send(file):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cliente')
    channel.basic_publish(exchange='', routing_key='cliente', body=file)
    connection.close()
