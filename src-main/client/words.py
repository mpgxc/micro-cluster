

def make_words_save(file):

    saida = open('words.txt','w')

    for line in file:
        saida.write(str(line)+"\n")
    saida.close()
