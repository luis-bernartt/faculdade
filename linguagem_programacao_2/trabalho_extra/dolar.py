import pandas as pd # type: ignore

file_path =  "/home/luis-bernartt/faculdade/linguagem_programacao_2/trabalho_extra/csv/dolar.csv"
dados = pd.read_csv(file_path, sep=';')

count = 0
total = 0

for index, row in dados.iterrows():
    if row['data'].startswith('2010'):
        total += float(row['cotacaoCompra'])
        count += 1

total_media = total / count

print(f'A média do dólar em 2010 é: {total_media:.2f}')