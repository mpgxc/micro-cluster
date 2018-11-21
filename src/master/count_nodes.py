

def make_count(file):

    count = 0
    for __ in open(file):
        count += 1
    return count
