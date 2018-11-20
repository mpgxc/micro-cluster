import pika
from read_load import load

def send(file):

    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='master')

    channel.basic_publish(exchange='', routing_key='master', body = file)
    connection.close()

def receive():

    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cliente')


    def callback(ch, method, properties, body):
        print(" [x] Recebido Cliente %r" % body)

        Saida = open('data.txt','w')
        Saida.write(str(body.decode()))
        Saida.close()

    channel.basic_consume(callback, queue='cliente', no_ack=True)
    channel.start_consuming()
    channel.stop_consuming()
    return None