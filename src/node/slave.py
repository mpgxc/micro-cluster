import zmq as mySocket
import sys
import threading
import json
import time
import base64
import zlib
from json_to_txt import make as json_txt
from save_file import save_txt
from mapper import mapper
from sorting import sorting
from reducer import reducer


def descompacta(text):
    return zlib.decompress(text)


def compacta(text):
    return zlib.compress(text)


class ClientTask(threading.Thread):

    def __init__(self, id):
        self.id = id
        threading.Thread.__init__(self)

    def run(self):

        context = mySocket.Context()
        socket = context.socket(mySocket.DEALER)
        identity = u'worker-%d' % self.id
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5575')

        print('Cliente %s INICIALIZADO' % (identity))

        poll = mySocket.Poller()
        poll.register(socket, mySocket.POLLIN)

        socket.send_json('Hit')

        msg = socket.recv()  # converte de String para JSON

        descompactado = descompacta(msg)  # descompactando texto

        decifrado = base64.b64decode(descompactado)  # decifra mensagem

        msg = eval(decifrado.decode('utf-8'))
        print(msg)
        # salvando texto json no arquivo de texto.txt

        save_txt(
            json_txt(
                msg
            )
        )

        # Agora proximo paso é mapear com 'mapper.py'
        mapper('cache/data.txt')
        # Agora temos que fazer o sorting
        sorting('cache/mapper_output.txt')
        # Agora é hora de aplicar o 'reducer.py'
        reducer('cache/mapper_output.txt')


        results = [line for line in open('cache/reducer_output.txt')]
        cifrado = base64.b64encode(str(
            results
        ).encode('utf-8'))


        compactado = compacta(cifrado)

        socket.send(compactado) #Enviando o resultado do reducing pro Master

        socket.close()
        context.term()


def main():

    client = ClientTask(100)
    client.start()


if __name__ == "__main__":
    main()
