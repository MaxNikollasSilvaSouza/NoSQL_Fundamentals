import modelo
import mongoempy

cidade = input('Quais jogadores moram na cidade: ')
pais = input('Quais jogadores moram no pais: ')
peso = input('Dos jogadores que moram no pais acima, quais pesam mais do que: ')


meio = input("Digite 1 para realizar a busca utilizando o PyMongo ou digite 2 para realizar a busca utilizando Mongo Engine: ")

#Pesquisa as informações utilizando PyMongo
if(int(meio) == 1):
    mongoempy.encontrar_cidade(cidade)
    print("\n\n\n")
    mongoempy.encontrar_pais_peso(pais,peso)
    print("\n\n\n")
    mongoempy.encontrar_posicao_jog()
    print("\n\n\n")
    mongoempy.listinha_times()

#Pesquisa as informações utilizando MongoEngine
elif(int(meio) == 2):
    modelo.encontrar_cidade(cidade)
    print("\n\n\n")
    modelo.encontrar_pais_peso(pais,peso)
    print("\n\n\n")
    modelo.encontrar_posicao_jog()
    print("\n\n\n")
    modelo.listinha_times()

else:
    print('Opção não válida')

