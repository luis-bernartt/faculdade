import pandas as pd  # type: ignore

class AcrePopulacao:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.dados = pd.read_csv(self.file_path, sep=',')

    def calcular_populacao(self) -> int:
        total_pop = 0
        for _, row in self.dados.iterrows():
            if row['STATE'] == 'AC':
                total_pop += int(row['IBGE_POP'])
        return total_pop
