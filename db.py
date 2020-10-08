from pymongo import MongoClient
import csv

class Dbase(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = client['bbva']


    def load_db_clients(self):
        clientes = db['clientes']
        with open('baseClientesHackaton8Oct', 'r') as f:
            for lin in csv.DictReader(f):
                clintes.insert_one(lin)

    def load_db_users(self):
        clientes = db['clientes']
        with open('baseUsuarios', 'r') as f:
            for lin in csv.DictReader(f):
                clintes.insert_one(lin)

dbc = Dbase()
dbc.load_db_clients()
