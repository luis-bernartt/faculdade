import pandas as pd # type: ignore

file_path =  "/home/luis-bernartt/faculdade/linguagem_programacao_2/trabalho_extra/repository/cidades_do_brasil.csv"

dados = pd.read_csv(file_path, sep=',')

total_pop = 0

for index, row in dados.iterrows():
    if row['STATE'] == 'AC':
        total_pop += int(row['IBGE_POP'])

print(f'A população do Acre é: {total_pop}')