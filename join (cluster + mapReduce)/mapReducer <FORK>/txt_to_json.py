


def make(url):
    return [{"text": line}   for line in open(url)]
'''
for line in make("data.txt"):
    print(line['text'])
'''
