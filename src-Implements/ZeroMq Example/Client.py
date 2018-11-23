import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:3333")

socket.send_string("Olá")
