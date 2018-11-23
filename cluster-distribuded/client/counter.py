
import random, time
from functools import wraps


def Count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        TimeOne = time.time()
        Result = func(*args, **kwargs)
        TimeTwo = time.time()
        Tempo = str(TimeTwo - TimeOne) #Minha contribuição ao código
        print("Função:",func.__name__)
        if (float(Tempo)) >= 60:
            print("Tempo de Execução: ",float(Tempo)/60,"min")
        elif Tempo[len(Tempo) - 3] == '-':
            print("Tempo de Execução: ",Tempo,"ms")
        else:
            print("Tempo de Execução: ",Tempo,"sec")
        return Result
    return wrapper
