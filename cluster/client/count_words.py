
def count_words():

    result = []
    count = 0
    for index in open('words.txt'):
        
        result.append((index.replace("\n",""), 0))

        for line in open('data.txt'):
            
            data = line.split()

            if data[0].lower() == index.replace("\n","").lower():
                result[count] = data
            
        count += 1

    return result
