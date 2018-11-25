import zmq as mySocket
import sys
import threading
import json
import time
import base64
import time
import timeit
from readdata import load
import zlib
from txt_to_json import make as data_json
from jack_module import make_jack
import os
from final_reducer import reducer
from sorting import sorting as make_order
from sender import server_Envia
from call_nodes import connectNodes
from count_nodes import make_count
from sender import server_Recebe
from insert_values import insert_relats


def descompacta(text):
    return zlib.decompress(text)


def compacta(text):
    return zlib.compress(text)


def tprint(msg):

    sys.stdout.write(msg + '\n')
    sys.stdout.flush()


class ServerTask(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        context = mySocket.Context()
        frontend = context.socket(mySocket.ROUTER)
        # frontend.bind('tcp://192.168.0.3:5599')
        frontend.bind('tcp://*:12345')

        backend = context.socket(mySocket.DEALER)
        backend.bind('inproc://backend')

        # workers = []

        worker = ServerWorker(context)
        worker.start()
        # workers.append(worker)

        mySocket.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()


class ServerWorker(threading.Thread):

    def __init__(self, context):
        threading.Thread.__init__(self)
        self.context = context

    def run(self):

        while True:

            print("Iniciando Server-Recebe Requests")
            server_Recebe()  # Ativa o SocketMQ para receber requisições

            worker = self.context.socket(mySocket.DEALER)
            worker.connect('inproc://backend')
            tprint('Servidor TRABALAHNDO')

            # Faz uma chamada RPC, para conectar os nodes ao master
            quant_slave = make_count()

            print("++++++++++++++++++++++++++++++++")
            print("Nodes: ", quant_slave)
            print("++++++++++++++++++++++++++++++++")

            connectNodes()

            count = 0

            lastid = None

            myNodes = []

            while count < int(quant_slave):

                ident, msg = worker.recv_multipart()

                myNodes.append(ident)  # Guardando referência do meu node

                lastid = ident

                print("Worker: %s" % (ident.decode()))

                if lastid != ident.decode():
                    count += 1

            while True:
                time.sleep(0.5)
                print("< Esperando Receber DADOS! >")
                try:
                    myData = open("data.txt")
                    break
                except:
                    pass

            print("Leu Dados!")
            inicio = timeit.default_timer()

            # recebendo data e convertendo em JSOn
            data = data_json(
                [line for line in myData]
            )
            # montando clusters do arquivo recebido com base na quantidade de nodes do cluster
            parts = make_jack(int(quant_slave), data)  # PRESTA antenção aqui

            count_ident = 0

            for line in parts:
                    # aqui se cifra a mensagem em base64
                cifrado = base64.b64encode(str(line).encode('utf-8'))
                compactado = compacta(cifrado)

                # Enviando para cada node uma parte do arquivo
                worker.send_multipart([myNodes[count_ident], compactado])
                count_ident += 1

            count = 0

            while count < int(quant_slave):

                ident, msg = worker.recv_multipart()

                descompactado = descompacta(msg)  # descompactando texto
                decifrado = base64.b64decode(descompactado)  # decifra mensagem

                out = open('cache/mapper_output.txt', 'a')
                # EVAL converte bytes em Array List
                for line in eval(decifrado):
                    out.write(str(line))

                count += 1

            out.close()

            # Sorting results mapper
            make_order('cache/mapper_output.txt')
            # executa o final reducing
            reducer('cache/mapper_output.txt')
            # CountTempo

            fim = timeit.default_timer()

            Tempo = fim - inicio

            if (float(Tempo)) >= 60:
                result = str(float(Tempo)/60) + "-" + "Minutos"

            elif str(Tempo)[len(str(Tempo)) - 3] == '-':
                result = str(Tempo) + "-" + "Milisegundos"

            else:
                result = str(Tempo) + "-" + "Segundos"
            # Envia pro cliente
            server_Envia(
                "".join([line for line in open(
                    'cache/reducer_output.txt')]), str(result)
            )
            # insere no banco de dados

            Pals = open('query_words.txt','r').readlines()
            Pals = str(Pals)
            print(Pals)
            print(Pals[0], Pals[1], Pals[2])
            
            insert_relats(str(result), Pals[0], Pals[1], Pals[2])

            # Deletando file tmp
            os.remove('cache/mapper_output.txt')
            os.remove('cache/reducer_output.txt')
            os.remove('data.txt')

            try:
                os.remove('cache/status.txt')
            except:
                pass

            print("Complete Task!")

            worker.close()


def main():

    server = ServerTask()
    server.start()
    server.join()
