from readdata import load

def make(url):
    return [{"text": line}   for line in url]


'''
count = 0
for line in make(load()):
    print(count, line['text'])
    count += 1

'''