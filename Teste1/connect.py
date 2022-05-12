from pymongo import MongoClient

#testa a conexao
client = MongoClient("localhost",27017)



#cria a base de dados

try:
    db = client.trilha_mongodb
except:
    print("")

#inserindo valores
def salvar(linha):
    
    try:
        db.colecao.insert([linha])
    except Exception:
        print(Exception)

