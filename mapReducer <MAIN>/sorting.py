
def sorting():

    out = open('saida.txt', 'r+')
    data = [line.strip() for line in open('saida.txt')]
    data.sort()
    for line in data:
        out.write(str(line)+"\n")
    out.close()

if __name__ == '__main__':
    sorting()