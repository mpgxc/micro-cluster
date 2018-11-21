from flask import Flask, render_template, request, redirect, url_for
from sender import send, receive
from forms import Entrada
from read_load import load
import requests
import time
import multiprocessing
import threading
import os
app = Flask(__name__)


def task_connection():

    tasK = threading.Thread(name="t1", target=receive)
    tasK.start()


@app.route('/', methods=['GET', 'POST'])
def index():

    campos = Entrada(request.form)
    palavras = str(campos.Palavras.data)
    texto = str(campos.Texto.data)

    if palavras == '' or texto == '':
        print('Faz nada!')
    else:

        send(texto)
        task_connection()

        return redirect(url_for('update'))

    return render_template('index.html', campos=campos)


@app.route('/update')
def update():

    while True:
        try:
            if load('data.txt') == []:
                pass
            else:
                data_set = load('data.txt')
                break
        except:
            pass
    os.remove('data.txt')
    
    return render_template('update.html', data=data_set)


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8076, debug=True)
