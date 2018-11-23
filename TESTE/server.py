import pika
import os
import zmq
import random
import sys
import time

SERVER_CLIENT = 3333


def server_Recebe():

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://127.0.0.1:%s" % (SERVER_CLIENT))

    
    sec = socket.recv_string()
    msg = socket.recv()

    print("Tempo:", sec)
    print("Recebido:", msg.decode("utf-8"))

    Saida = open("data.txt", "w")
    Saida.write(str(msg.decode("utf-8")))
    Saida.close()


server_Recebe()