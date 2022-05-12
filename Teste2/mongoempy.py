from pymongo import MongoClient

#Conexão com o banco
client = MongoClient()
db = client['trilha_mongodb']
collection = db['colecao']

#Encontra a cidade que voce deseja
def encontrar_cidade( cidade):
    print(f"Jogadores da cidade {cidade}: \n")
    for  registro in collection.find():
     if registro['TEAM_CITY'] == cidade:
         print(registro['NAME'] + "\n")

#Encontra o pais e o peso do jogador
def encontrar_pais_peso(pais, peso):
    print(f"Jogadores do pais: {pais} com peso maior que {peso}: \n")
    for  registro in collection.find():
     if registro['WEIGHT'] > peso and registro['COUNTRY'] == pais:
         print(f"Nome: {registro['NAME']} \t Pais: {registro['COUNTRY']} \t Peso: {registro['WEIGHT']}")

#Encontra a posição do jogador
def encontrar_posicao_jog():
    print('Jogadores que atuam em posição "Center" ou "Guard": ') 
    for  registro in collection.find():
     if registro['POSITION'] == 'Center' and registro['POSITION'] == 'Guard':
         print(f"Nome: {registro['NAME']} \t Posição: {registro['POSITION']}")
         
#Lista o ID do time  e seus respectivos estados
def listinha_times():
   
    listinha =[]
    for  registro in collection.find():
     if registro['TEAM_ID'] not in listinha:         
         listinha.append(registro['TEAM_ID'])

    contador = -1
    print('Lista de times e seus respectivos estados\n')
    try:
        for estado in listinha:
            contador+=1
            
            #print(f"\nEstado: {estado}\n\nTimes:\n")   
            for  registro in collection.find():                
                if registro['TEAM_ID'] == listinha[contador]:                 
                    print(f"{registro['TEAM_ID']} \t  {registro['TEAM_STATE']}\n")
                    contador+=1
    except Exception:
        print("")





