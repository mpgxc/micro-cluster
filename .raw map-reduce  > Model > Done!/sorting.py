import sys

def sorting():

    out = open(sys.argv[1], 'r+')
    data = [line.strip() for line in open(sys.argv[1])]
    data.sort()
    for line in data:
        out.write(str(line)+"\n")
    out.close()

if __name__ == '__main__':
    sorting()