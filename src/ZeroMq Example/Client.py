import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:3333")

socket.send_string("""
                    Ela era bruxa, ele era um lobo.
                   Ambos prontos para amar.
                   Ela tão clara, ele tão escuro.
                   Ambos em busca de se encontrar.
                   Ele corria, e ela fugia.
                   A noite ele aparecia com seu uivo dolorido.
                   E ela surgia a iluminar a noite com o luar.
                   A bruxa era vida e o Lobo o destino.
                   Ambos seguiam pro mesmo lugar.
                   Da morte fugiam.
                   Os dois dividiam o mesmo caminho.
                   Eles não tinham medo, nem dor e nem desespero!
                   Tentam fazer de tudo para ficar juntos
                   A vida e o destino num mesmo amor.
                   E quando o impossível tornar-se possível
                   Tão perto um do outro, eles irão ficar.
                   Todos nesse dia vão descobrir
                   A essência de todo esse amor.
                   Desse amor impossível
                   Presente em nossa mente
                   Pois eles sabem que tudo terá seu lugar,
                   Sua data marcada, sua hora exata.
                   Se for pra ser, será.
                   E o impossível vai tornar-se possível
                   E ai um grande amor todos vão conhecer e eternizar."""
                   )
