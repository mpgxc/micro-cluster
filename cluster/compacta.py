import zlib


def compacta(text):
    return zlib.compress(text)

def descompacta(text):
    return zlib.decompress(text)