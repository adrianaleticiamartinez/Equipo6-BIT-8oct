#from pymongo import MongoClient
import csv, json
from firebase import firebase


class Dbase(object):
    def __init__(self):
        self.client = None#MongoClient('mongodb+srv://bbvatest:bbvatest@cluster0.uvfsh.mongodb.net/<dbname>?retryWrites=true&w=majority')
        #self.db = self.client['bbva']
        #self.clientes = self.db['clientes']
        #self.usuarios = self.db['usuarios']
        self.fb = firebase.FirebaseApplication('https://bbva-a1ba8.firebaseio.com', None)

        self.rst = {
        'idCliente': 0, 'nombre': 0, 'apellidoPaterno': 1, 'apellidoMaterno': 1,
        'fechaNacimiento': 1, 'sexo': 0,
        'segmento': 0,
        'nacionalidad': 1, 'rfc': 1,
        'tipoID': 1, 'numeroID': 1, 'cuenta': 0, 'email': 1
        }

    def get_client(self, cliente):
        #return self.clientes.find_one({"idCliente": cliente})
        return self.fb.get('/users/1', None, {'idCliente': cliente})

    def get_user(self, user):
        with open('baseUsuarios.csv', 'r', encoding = 'utf-8') as f:
            for lin in csv.DictReader(f):
                #print('user', lin)
                if lin['\ufeffusuario'] == user['usuario'] and lin['auth'] == lin['auth']:
                    return lin
                return {}

    def load_db_clients(self):

        with open('baseClientesHackaton8Oct.csv', 'r', encoding = 'utf-8') as f:
            for lin in csv.DictReader(f):
                #lin = {x: lin[x].encode('utf-8') for x in lin}
                #print('lin', lin)
                #self.clientes.insert_one(lin)
                yield lin


    def add_json(self):
        with open('clientes.json', 'w') as f:
            json.dump(list(self.load_db_clients()), f)

    #def load_db_users(self):
    #    clientes = db['usuarios']
    #    with open('baseUsuarios.csv', 'r') as f:
    #        for lin in csv.DictReader(f):
    #            self.usuarios.insert_one(lin)

if __name__ == "__main__":
    dbc = Dbase()
    dbc.add_json()
