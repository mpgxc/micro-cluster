from mapper import mapper

'''
    Essa função monta clusters como base no números de nodes do Cluster.. Simples
    Caso o cluster possuir até 3 nodes, o json é dividido em 3 partes, e enviado para cada node, para assim ser trabalhado
'''

def make_jack(num_worker, file):
    '''
        A divisão do arquivo depende da quantidade de máquinas liagadas ao cluster
        num_worker corresponde a esse número de máquinas.
    '''
    qtd = len(file)
    workers = int(qtd/num_worker)
    count = 0

    result = []
    clusters = []

    for line in file:

        result.append(line)

        count += 1

        if count == workers:

            result = sorted(result, key = lambda i: i['text']) #linha pra ordenar JSON baseao no campo de texto
    
            clusters.append(result)

            result = []
            
            workers += int(qtd/num_worker)

    return clusters


#como usar
for line in make_jack(3 , mapper("portuguese","data.txt")):
    print(line)
    print("----------------------")