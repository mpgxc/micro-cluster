import pika 
import os



def send(file):

    url = os.environ.get(
        'CLOUDAMQP_URL', 'amqp://ccamejce:pXan0kUexXzAYv3k92uIzCfjATB9QMF4@porpoise.rmq.cloudamqp.com/ccamejce'
    )

    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue="cliente")  # Declare a queue
    channel.basic_publish(exchange='', routing_key="cliente", body=file)
    connection.close()

