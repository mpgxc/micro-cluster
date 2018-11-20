import sys

def sorting(file):

    out = open(file, 'r+')
    data = [line.strip() for line in open(file)]
    data.sort()
    for line in data:
        out.write(str(line)+"\n")
    out.close()
