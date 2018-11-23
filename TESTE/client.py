import pika
import os
import zmq
import random
import sys
import time

SERVER_MASTER = 3333


def server_Envia(file):

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://127.0.0.1:%s" % (SERVER_MASTER))
    
    socket.send_string("2.3463768941345")
    socket.send_string(file)


server_Envia("teste\tolá ksd ksd\n \n \nhgghfhg ")