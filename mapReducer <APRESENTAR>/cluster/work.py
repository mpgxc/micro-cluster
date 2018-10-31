



out = open("saida.txt","w")

def make():

    for line in range(10):
        out.write(str(line) + "\tCluster"+"\n")

make()