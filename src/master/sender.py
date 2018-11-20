import pika 


def send(file):

    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cliente')

    channel.basic_publish(exchange='', routing_key='cliente', body = file)
    print(" [x] Enviado")
    connection.close()