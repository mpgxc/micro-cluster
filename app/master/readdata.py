
def load(file = "data.txt"):

    data = []
    for line in open(file):
        data.append(line)
    return data
 