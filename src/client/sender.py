import pika


def send(file):

    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='master')

    channel.basic_publish(exchange='', routing_key='master', body = file)
    print(" [x] Enviado")
    connection.close()

def receive():

    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cliente')


    def callback(ch, method, properties, body):
        print(" [x] Recebido %r" % body)

        Saida = open('data.txt','w')
        Saida.write(str(body.decode()))

    channel.basic_consume(callback, queue='cliente', no_ack=True)
    channel.start_consuming()

    return -1
