from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document

#Conexão com o banco de dados
mongoengine.connect(host = "mongodb://localhost:27017/mongodb")

#Armazena os dados
class Colecao(Document):
    ROW =mongoengine.StringField()
    ID = mongoengine.StringField()
    ACTIVE = mongoengine.IntField()
    NAME = mongoengine.StringField()
    COUNTRY = mongoengine.StringField()
    HEIGHT = mongoengine.StringField()
    WEIGHT = mongoengine.StringField()
    POSITION = mongoengine.StringField()
    TEAM_ID = mongoengine.IntField()
    TEAM_CITY = mongoengine.StringField()
    TEAM_STATE = mongoengine.StringField()
    PLAYER_SALARY_SEASON = mongoengine.StringField()
    PLAYER_SALARY_AMOUNT = mongoengine.StringField()


#try:

  #  for post in Colecao.objects(ID="76001"):
 #       print(post.ID, post.ROW, post.NAME)
#except Exception:
   # print(str(Exception))


#Encontra a cidade que voce deseja
def encontrar_cidade(cidade):
    print(f"Jogadores da cidade {cidade}: \n")
    for  registro in Colecao.objects(TEAM_CITY = cidade):
        if registro['TEAM_CITY'] == cidade:
            print(registro['NAME'] + "\n")

#Encontra o pais e o peso do jogador
def encontrar_pais_peso(pais, peso):
    print(f"Jogadores do pais: {pais} com peso maior que {peso}: \n")
    for  registro in Colecao.objects():
     if registro['WEIGHT'] > peso and registro['COUNTRY'] == pais:
         print(f"Nome: {registro['NAME']} \t Pais: {registro['COUNTRY']} \t Peso: {registro['WEIGHT']}")

#Encontra a posição do jogador
def encontrar_posicao_jog():
    print('Jogadores que atuam em posição "Center" ou "Guard": ') 
    for  registro in Colecao.objects():
     if registro['POSITION'] == 'Center' and registro['POSITION'] == 'Guard':
         print(f"Nome: {registro['NAME']} \t Posição: {registro['POSITION']}")


#Lista o ID do time  e seus respectivos estados
def listinha_times():
   
    listinha =[]
    for  registro in Colecao.objects():
     if registro['TEAM_ID'] not in listinha:         
         listinha.append(registro['TEAM_ID'])

    contador = -1
    print('Lista de times e seus respectivos estados\n')
    try:
        for estado in listinha:
            contador+=1
            
            #print(f"\nEstado: {estado}\n\nTimes:\n")   
            for  registro in Colecao.objects():                
                if registro['TEAM_ID'] == listinha[contador]:                 
                    print(f"ID: {registro['TEAM_ID']} \t  {registro['TEAM_STATE']}\n")
                    contador+=1
    except Exception:
        print("")