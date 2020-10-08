from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/clients/<client>')
def get_info(client):
    return 'Hello, World %s' % (client)
