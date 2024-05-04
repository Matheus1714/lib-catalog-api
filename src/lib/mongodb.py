from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['db']

collection = db['any']

collection.insert_one({ "chave": "teste" })

docs = collection.find()

for doc in docs:
    print(doc)