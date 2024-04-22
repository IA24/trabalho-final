from interface import Interface
from algoritmos.a_estrela import AEstrela
from algoritmos.custo_uniforme import CustoUniforme
from data import CONEXOES, PAISES, LOCALIZACOES


def main():
    #Interface.interface()

    teste_custouniforme()
    teste_aestrela()


def teste_aestrela():
    search = AEstrela("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


def teste_custouniforme():
    search = CustoUniforme("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


main()
