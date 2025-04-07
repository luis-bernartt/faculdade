import pandas as pd  # type: ignore

class CrimeMaisComum:
    def __init__(self, file_path: str, estado: str):
        self.file_path = file_path
        self.estado = estado
        self.dados = pd.read_csv(self.file_path, sep=',')

    def crime_mais_frequente(self) -> str:
        dados_estado = self.dados[self.dados['Uf'] == self.estado]
        tipo_crime = pd.DataFrame(dados_estado['Tipo_crime']).drop_duplicates()
        tipo_crime['quantidade'] = 0

        count = 0
        tipo_mais_comum = ''

        for _, row in dados_estado.iterrows():
            for index2, tipo in tipo_crime.iterrows():
                if row['Tipo_crime'] == tipo['Tipo_crime']:
                    tipo_crime.at[index2, 'quantidade'] += 1
                    if tipo_crime.at[index2, 'quantidade'] > count:
                        count = tipo_crime.at[index2, 'quantidade']
                        tipo_mais_comum = tipo['Tipo_crime']
        return tipo_mais_comum