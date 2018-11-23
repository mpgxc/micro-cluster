from socket import *
network = '192.168.0.'


def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)
    if not s.connect_ex((addr, 135)):
        s.close()
        return 1
    else:
        s.close()


def map_network():
    
    lista = []
    for ip in open("cache/nodes.txt"):
       lista.append(ip)
    return lista
