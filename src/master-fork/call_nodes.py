import zerorpc


def connectNodes():
    #tem que uma lista dos ips com um laço de repetição
    Connect = zerorpc.Client()
    Connect.connect("tcp://127.0.0.1:5432")
    Connect.start(100)