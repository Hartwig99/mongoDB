pip install pymongo

import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017/")

banco_de_dados = cliente["exemplo_banco_de_dados"]

colecao = banco_de_dados["exemplo_colecao"]


documento = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
colecao.insert_one(documento)


documentos = colecao.find()
for documento in documentos:
    print(documento)
