

def count_lines(file):
    return sum(1 for __ in open(file))

def make_jack(num_worker, file = 'saida.txt'):
    '''
        A divisão do arquivo depende da quantidade de máquinas liagadas ao cluster
        num_worker corresponde a esse número de máquinas.
    '''
    qtd = count_lines(file)
    workers = int(qtd/num_worker)
    count = 0

    result = []
    clusters = []

    for line in open(file):

        result.append(line.replace('\n',''))
        count += 1

        if count == workers:
            clusters.append(result)
            result = []
            workers += int(qtd/num_worker)

    return clusters

def simulate_worker():

    count = 1
    
    for line in make_jack(3):
        
        out = open('worker_'+str(count),'w')

        for index in line:
            out.write(index+'\n')
        out.close()
        count += 1

simulate_worker()