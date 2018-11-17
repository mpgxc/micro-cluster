from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/worker')
def update():
    return render_template('worker.html')

if __name__ == '__main__':
    app.run(debug=True)