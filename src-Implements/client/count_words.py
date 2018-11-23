
def count_words():

    result = []
    for index in open('words.txt'):
        for line in open('data.txt'):
            
            data = line.split()
            if data[0] == index.replace("\n", ""):
                result.append(data)

    return result