from operator import itemgetter
import sys


def reducer(file):

    current_word = None
    current_count = 0
    word = None

    out = open('final.txt', 'a')

    for line in file:

        line = line.strip()

        word = line['text']
        count = line['count']

        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count

        else:
            if current_word:
                print('%s\t%s' % (current_word, current_count))
                out.write('%s\t%s' % (current_word, current_count)+'\n')
            current_count = count
            current_word = word

    if current_word == word:
        print('%s\t%s' % (current_word, current_count))
        out.write('%s\t%s' % (current_word, current_count)+'\n')
    out.close()


if __name__ == '__main__':
    reducer()
