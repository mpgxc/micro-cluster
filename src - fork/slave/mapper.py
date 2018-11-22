from preprocess import make_tokens


def mapper(file):

    lang = 'portuguese'
    out = open("cache/mapper_output.txt", "w")

    for line in open(file):

        tweet = make_tokens(line, lang)
        tweet = tweet.strip()
        words = tweet.split()

        for word in words:
            out.write('%s\t%s' % (word, 1)+"\n")