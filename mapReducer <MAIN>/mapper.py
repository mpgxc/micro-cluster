from preprocess import make_tokens

def mapper(lang='portuguese'):

    out = open("saida.txt", "w")
    for line in open('data.txt'):

        tweet = make_tokens(line, lang)
        tweet = tweet.strip()
        words = tweet.split()
        
        for word in words:
            print('%s\t%s' % (word, 1))
            out.write('%s\t%s' % (word, 1)+"\n")

if __name__ == "__main__":
    mapper('english')
