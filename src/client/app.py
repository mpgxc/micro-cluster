from flask import Flask, render_template, request
import requests
import time 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update')
def update():
    data = "Mateus Pintos Garcia"
    time.sleep(5)
    return render_template('update.html', data = data )


@app.route('/spiner')
def spiner():
    return render_template('spiner.html')

if __name__ == '__main__':
    app.run(debug=True)