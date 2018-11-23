import zmq
import random
import sys
import time


def server_Recebe():

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://127.0.0.1:3333")

    msg = socket.recv()
    print("Recebido:", msg.decode("utf-8"))

    Saida = open("data.txt", "w")
    Saida.write(str(msg.decode("utf-8")))
    Saida.close()


server_Recebe()
