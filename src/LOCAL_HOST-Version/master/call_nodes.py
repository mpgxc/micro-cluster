import zerorpc


def get_ips():
    lista = []
    codes = []

    for line in open("cache/ips.txt"):
        ip, code = line.split("-")
        lista.append(ip.replace("\n", ""))
        codes.append(code.replace("\n", ""))

    return lista, codes


def connectNodes(quant):

    start = 0
    ips, codes = get_ips()

    data = open("cache/nodes.txt", "w")

    while start < int(quant):
        print("*")
        Connect = zerorpc.Client()
        Connect.connect("tcp://"+str(ips[start])+":9000")

        data.write(str("worker-%s" % (codes[start]))+"\n")

        Connect.start(codes[start])

        start += 1

    data.close()
