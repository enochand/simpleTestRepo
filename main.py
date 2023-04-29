from flask import Flask, render_template
from flask_sock import Sock
import json

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        print(type(data), data)
        message = {'test': 1}
        message = json.dumps(message)
        sock.send(message)
app.run(host='0.0.0.0', port=8080)