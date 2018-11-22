from flask import Flask, render_template, request, redirect, url_for
from sender import send, receive
from forms import Entrada
from read_load import load
import requests
import time
import multiprocessing
import threading
import os
from words import make_words_save
from count_words import count_words

app = Flask(__name__)


def task_connection():

    tasK = threading.Thread(name="t1", target=receive)
    tasK.start()


@app.route('/', methods=['GET', 'POST'])
def index():

    campos = Entrada(request.form)

    pal1 = str(campos.Palavras1.data)
    pal2 = str(campos.Palavras2.data)
    pal3 = str(campos.Palavras3.data)

    texto = str(campos.Texto.data)

    if pal1 == '' or pal2 == '' or pal3 == '' or texto == '':
        pass
    else:

        send(texto)
        task_connection()

        time.sleep(0.5)

        make_words_save([pal1, pal2, pal3])  # Palavras bases para pesquisar

        return redirect(url_for('update'))

    return render_template('index.html', campos=campos)


import time
import timeit


@app.route('/update')
def update():
    # tem como melhorar, mas não vai ser agora....

    inicio = timeit.default_timer()

    while True:
        time.sleep(1)
        try:
            if load('data.txt') == []:
                pass
            else:
                data_set = load('data.txt')
                break
        except:
            pass

    fim = timeit.default_timer()

    result = fim - inicio

    pals = count_words()

    os.remove('data.txt')
    os.remove('words.txt')

    return render_template('update.html', data=data_set, pals=pals, tempo=str(result))


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8076, debug=True)
