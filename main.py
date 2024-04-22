from algoritmos.profundidade_limitada import ProfundidadeLimitada
from interface import Interface
from algoritmos.a_estrela import AEstrela
from algoritmos.custo_uniforme import CustoUniforme
from data import CONEXOES, PAISES, LOCALIZACOES


def main():
    #Interface.interface()

    print("Profundidade Limitada")
    teste_profundidadelimitada()
    print("\n---------------------------------------\n")
    print("Custo Uniforme")
    teste_custouniforme()
    print("\n---------------------------------------\n")
    print("A Estrela")
    teste_aestrela()


def teste_profundidadelimitada():
    search = ProfundidadeLimitada("Coimbra", "Faro", 5)
    resultado = search.algoritmo()
    resultado.display()


def teste_aestrela():
    search = AEstrela("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


def teste_custouniforme():
    search = CustoUniforme("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


main()
