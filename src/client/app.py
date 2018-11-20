from flask import Flask, render_template, request, redirect, url_for
from sender import send, receive
from forms import Entrada
from read_load import load
import requests
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    campos = Entrada(request.form)
    palavras = str(campos.Palavras.data)
    texto = str(campos.Texto.data)

    if palavras == '' or texto == '':
        print('Faz nada!')
    else:
        
        send(texto)
        receive()
        data_set = load('data.txt')

        return redirect(url_for('update', data_set = data_set))
    return render_template('index.html', campos = campos)


@app.route('/update')
def update():
    return render_template('update.html')


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8075, debug=True)
