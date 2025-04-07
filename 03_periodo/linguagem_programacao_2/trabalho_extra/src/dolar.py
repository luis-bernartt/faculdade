import pandas as pd  # type: ignore

class DolarMedia:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.dados = pd.read_csv(self.file_path, sep=';')

    def media_dolar_ano(self, ano: str) -> float:
        count = 0
        total = 0.0

        for _, row in self.dados.iterrows():
            if row['data'].startswith(ano):
                total += float(row['cotacaoCompra'])
                count += 1

        return total / count if count > 0 else 0.0