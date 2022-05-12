import connect 
import pandas as pd

#Pega o caminho da arquivo com extensão tsv
data = pd.read_table(r"Caminho")

#realiza o laço pegando linha por linha da tabela
try:
        
    for contador in range(len(data)):
        
        l_row = data['ROW'][contador]
    
        l_id = data['ID'][contador]

        l_active = data['ACTIVE'][contador]
    
        l_name = data['NAME'][contador]
    
        l_country = data['COUNTRY'][contador]

        l_height = data['HEIGHT'][contador]
    
        l_weight = data['WEIGHT'][contador]

        l_position = data['POSITION'][contador]
    
        l_team_id = data['TEAM_ID'][contador]
    
        l_team_city = data['TEAM_CITY'][contador]
    
        l_team_state = data['TEAM_STATE'][contador]
    
        l_player_salary_season = data['PLAYER_SALARY_SEASON'][contador]
    
        l_player_salary_amount = data['PLAYER_SALARY_AMOUNT'][contador]
    
        #transforma em json
        linha = {'ROW':f'{l_row}', 'ID': f'{l_id}', 'ACTIVE':f'{l_active}', 'NAME':f'{l_name}', 'COUNTRY':f'{l_country}', 'HEIGHT':f'{l_height}', 'WEIGHT':f'{l_weight}', 'POSITION':f'{l_position}', 'TEAM_ID':f'{l_team_id}', 'TEAM_CITY':f'{l_team_city}', 'TEAM_STATE':f'{l_team_state}', 'PLAYER_SALARY_SEASON':f'{l_player_salary_season}', 'PLAYER_SALARY_AMOUNT':f'{l_player_salary_amount}'}
        #print(linha)

        #salva no banco mongoDB
        connect.salvar(linha)

    print("Dados Inseridos com sucesso!!!")

except Exception:
    print(Exception)

        