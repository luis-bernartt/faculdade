import pandas as pd # type: ignore

file_path =  "/home/luis-bernartt/faculdade/03_periodo/linguagem_programacao_2/trabalho_extra/repository/crimes_brasil_uf.csv"


dados = pd.read_csv(file_path, sep=',')

dados = dados[dados['Uf'] == 'Rio de Janeiro']

tipo_crime = pd.DataFrame(dados['Tipo_crime']).drop_duplicates()
tipo_crime['quantidade'] = 0
count = 0

for index, row in dados.iterrows():
    for index2, tipo in tipo_crime.iterrows():
        if row['Tipo_crime'] == tipo['Tipo_crime']:
            tipo['quantidade'] += 1
            if tipo['quantidade'] > count:
                count = tipo['quantidade']
                tipo_mais_comum = tipo['Tipo_crime']

print(f'O crime mais comum é: {tipo_mais_comum}')