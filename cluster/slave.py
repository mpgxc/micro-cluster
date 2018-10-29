import zmq
import sys
import threading
import json
import time
import base64
import compacta as makeCompactada


def tprint(msg):

    sys.stdout.write(msg + '\n')
    sys.stdout.flush()


class ClientTask(threading.Thread):

    def __init__(self, id):
        self.id = id
        threading.Thread.__init__(self)

    def run(self):

        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        identity = u'worker-%d' % self.id
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5570')

        print('Cliente %s INICIALIZADO' % (identity))

        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)
        reqs = 0

        while True:

            reqs = reqs + 1
            print('Req #%d sent..' % (reqs))

            data = {
                "code": reqs,
            }

            socket.send_json(data)

            msg = socket.recv()  # converte de String para JSON

            descompactado = makeCompactada.descompacta(msg) #descompactando texto
            
            decifrado = base64.b64decode(descompactado)  # decifra mensagem

            msg = eval(decifrado.decode('utf-8'))

            tprint('Cliente %s recebido > %s ' % (identity, msg['resp']))

            time.sleep(1)

        socket.close()
        context.term()


def main():

    client = ClientTask(100)
    client.start()


if __name__ == "__main__":
    main()
