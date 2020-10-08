from flask import Flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
from flask import request, redirect, url_for
from db import Dbase
from flask import render_template, session
import json

dba = Dbase()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        us = {
            'usuario': request.form['user'],
            'auth': request.form['pass']
        }

        user = dba.get_user(us)
        session['perfil'] = user['perfil']
        print('us', user)
        if us:
            return redirect(url_for('consult'))

        else:
            return 'El usuario no existe'



    else:
        return render_template('login.html')


@app.route('/consult/', methods=['GET', 'POST'])
def consult():
    if request.method == 'POST':
        perfil = session['perfil']
        cliente = request.form.get('cliente')

        if not cliente:
            return render_template('consult.html')

        cl = dba.get_client(cliente)
        print('cl', cl)

        return json.dumps(cl)
    else:
        return render_template('consult.html')


# @app.route('/clients/<client>')
# def get_info(client):
#     return 'Hello, World %s' % (client)
