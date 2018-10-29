import zmq as myThread
import sys
import threading
import json
import time
import base64
import compacta as makeCompactada


def tprint(msg):

    sys.stdout.write(msg + '\n')
    sys.stdout.flush()


class ServerTask(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        context = myThread.Context()
        frontend = context.socket(myThread.ROUTER)
        frontend.bind('tcp://*:5570')

        backend = context.socket(myThread.DEALER)
        backend.bind('inproc://backend')

        #workers = []

        worker = ServerWorker(context)
        worker.start()
        # workers.append(worker)

        myThread.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()


class ServerWorker(threading.Thread):

    def __init__(self, context):
        threading.Thread.__init__(self)
        self.context = context

    def run(self):

        worker = self.context.socket(myThread.DEALER)
        worker.connect('inproc://backend')
        tprint('Servidor TRABALAHNDO')

        while True:

            ident, msg = worker.recv_multipart()
            result = json.loads(msg)

            tprint('Requisição [%s] Node [%s]' %
                   (result['code'], ident.decode()))

            print(msg)

            # -------------AQUI VAI FICAR A ENTRADA DOS DADOS---------------

            data1 = {
                "code": 500,
                "resp": "Opaa...",
            }
            data2 = {
                "code": 600,
                "resp": "Iai...",
            }

            # --------------------------------------------------------------

            # aqui se cifra a mensagem em base64
            cifrado1 = base64.b64encode(str(data1).encode('utf-8'))
            cifrado2 = base64.b64encode(str(data2).encode('utf-8'))

            compactado = makeCompactada.compacta(cifrado1)

            '''
            print("TEXTO CIFRADO 1:", cifrado1)
            print("TEXTO CIFRADO 2:", cifrado2)
            '''

            idWorker = ident.decode()

            
            worker.send_multipart([ident, compactado])
      

        worker.close()


def main():

    server = ServerTask()
    server.start()
    server.join()


if __name__ == "__main__":
    main()
