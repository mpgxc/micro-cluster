import zmq

SERVER_CLIENT = 4444
SERVER_MASTER = 3333


def server_Envia(file, times):

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://127.0.0.1:%s" % (SERVER_CLIENT))

    socket.send_string(times)
    socket.send_string(file)


def server_Recebe():

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://127.0.0.1:%s" % (SERVER_MASTER))

    pal = socket.recv_string()
    msg = socket.recv()

    Saida = open("query_words.txt", "w")
    Saida.write(str(pal))
    Saida.close()

    Saida = open("data.txt", "w")
    Saida.write(str(msg.decode("utf-8")))
    Saida.close()