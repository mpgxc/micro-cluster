
def save_txt(file):

    saida = open('cache/data.txt','a')
    for line in file:
        saida.write(str(line.replace('\n',''))+'\n')
    saida.close()