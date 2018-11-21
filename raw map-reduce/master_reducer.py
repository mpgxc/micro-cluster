from operator import itemgetter
import sys

def reducer():

    current_word = None
    current_count = 0
    word = None

    out = open('master_reducer','w')

    for line in open(sys.argv[1]):
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
                print('%s\t%s' % (current_word, current_count))
                out.write('%s,%s' % (current_word, current_count)+'\n')
            current_count = count
            current_word = word

    if current_word == word:
        print('%s\t%s' % (current_word, current_count))
        out.write('%s,%s' % (current_word, current_count)+'\n')
    out.close()


if __name__ == '__main__':
    reducer()