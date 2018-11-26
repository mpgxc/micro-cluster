
def count_words():

    result = []
    count = 0
    for index in open('words.txt'):

        result.append((index.replace("\n", ""), 0))

        for line in open('data.txt'):

            data = line.split()

            if data[0].lower() == index.replace("\n", "").lower():
                result[count] = data

        count += 1

    return result


def all_count():

    count = 0
    array = []
    for line in open("data.txt"):
        data = line.split()
        array.append([data[0], int(data[1])])
        count += 1
        if count == 15:
            break 
    return array
