import zmq as mySocket
import threading
import base64
import os
import zlib
from json_to_txt import make as json_txt
from save_file import save_txt
from mapper import mapper
from sorting import sorting
from reducer import reducer
import zerorpc


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
        identity = "worker-%d" % self.id
        socket.identity = identity.encode("ascii")
        socket.connect("tcp://localhost:12345")

        print("Cliente %s INICIALIZADO" % (identity))

        poll = mySocket.Poller()
        poll.register(socket, mySocket.POLLIN)

        socket.send_json("Hit")

        msg = socket.recv()  # converte de String para JSON

        descompactado = descompacta(msg)  # descompactando texto

        decifrado = base64.b64decode(descompactado)  # decifra mensagem

        msg = eval(decifrado.decode("utf-8"))
        print(msg)
        # salvando texto json no arquivo de texto.txt

        save_txt(json_txt(msg))

        # Agora proximo paso é mapear com 'mapper.py'
        mapper("cache/data.txt")
        # Agora temos que fazer o sorting
        sorting("cache/mapper_output.txt")
        # Agora é hora de aplicar o 'reducer.py'
        reducer("cache/mapper_output.txt")

        results = [line for line in open("cache/reducer_output.txt")]
        cifrado = base64.b64encode(str(results).encode("utf-8"))

        compactado = compacta(cifrado)

        socket.send(compactado)  # Enviando o resultado do reducing pro Master

        os.remove("cache/data.txt")
        os.remove("cache/mapper_output.txt")
        os.remove("cache/reducer_output.txt")

        socket.close()
        context.term()


class HelloRPC(object):

    def start(self, code):

        client = ClientTask(int(code))
        client.start()


if __name__ == "__main__":

    print("[ * ] - Servidor RPC - Slaver")

    Connect = zerorpc.Server(HelloRPC())
    Connect.bind("tcp://0.0.0.0:56789")
    Connect.run()
