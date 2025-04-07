from src.acre import AcrePopulacao
from src.criminalitie import CrimeMaisComum
from src.dolar import DolarMedia

if __name__ == "__main__":
    pop = AcrePopulacao("/home/luis-bernartt/faculdade/03_periodo/linguagem_programacao_2/trabalho_extra/repository/cidades_do_brasil.csv")
    print(f'A população do Acre é: {pop.calcular_populacao()}')

    crime = CrimeMaisComum("/home/luis-bernartt/faculdade/03_periodo/linguagem_programacao_2/trabalho_extra/repository/crimes_brasil_uf.csv", "Rio de Janeiro")
    print(f'O crime mais comum é: {crime.crime_mais_frequente()}')

    dolar = DolarMedia("/home/luis-bernartt/faculdade/03_periodo/linguagem_programacao_2/trabalho_extra/repository/dolar.csv")
    print(f'A média do dólar em 2010 é: {dolar.media_dolar_ano("2010"):.2f}')