from preprocess import make_tokens
import sys

def mapper(lang='portuguese'):

    out = open("saida3.txt", "w")
    for line in open(sys.argv[1]):

        tweet = make_tokens(line, lang)
        tweet = tweet.strip()
        words = tweet.split()
        
        for word in words:
            print('%s\t%s' % (word, 1))
            out.write('%s\t%s' % (word, 1)+"\n")

if __name__ == "__main__":
    mapper('english')
