def array():
    f = open("DATA-SET.txt",'r')
    texto = f.readlines()

    x = 0

    while x < len(texto):
        if texto[x] == "\n":
            local = texto.index(texto[x])
            texto.pop(local)
        else:
            texto[x] = texto[x].split('\t')
            x += 1


    for i in texto:
        local = texto.index(i)
        for b in i:
            local2 = texto[local].index(b)
            if "\n" in b:
                texto[local][local2] = b.replace("\n",'')
    return texto



def make(param, lista1):
    for index in param:
        for line in lista1:
            if index == line[0]:
                print("Ok... >>", line)
            else:
                pass
            

if __name__ == "__main__":
    make(["mateus","orrana","emanuel"], array())