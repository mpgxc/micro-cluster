import pika
import os
import zmq
import random
import sys
import time

SERVER_CLIENT = 4444
SERVER_MASTER = 3333


def server_Envia(file, palavras):

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://127.0.0.1:%s" % (SERVER_MASTER))
    socket.send_string(palavras)
    socket.send_string(file)


def server_Recebe():

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://127.0.0.1:%s" % (SERVER_CLIENT))

    sec = socket.recv_string()
    msg = socket.recv()

    Saida = open("time.txt", "w")
    Saida.write(str(sec))
    Saida.close()

    Saida = open("data.txt", "w")
    Saida.write(str(msg.decode("utf-8")))
    Saida.close()
