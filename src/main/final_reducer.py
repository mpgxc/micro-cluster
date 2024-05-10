from operator import itemgetter
import sys


def reducer(file):

    current_word = None
    current_count = 0
    word = None

    out = open('cache/reducer_output.txt', 'w')

    for line in open(file):
        line = line.strip()
        word, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count

        else:
            if current_word:
                out.write('%s\t%s' % (current_word, current_count)+'\n')
            current_count = count
            current_word = word

    if current_word == word:
        out.write('%s\t%s' % (current_word, current_count)+'\n')
    out.close()
