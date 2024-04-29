from algoritmos.profundidade_limitada import ProfundidadeLimitada
from algoritmos.procura_sofrega import ProcuraSofrega
from algoritmos.a_estrela import AEstrela
from algoritmos.custo_uniforme import CustoUniforme


def teste():
    print("Custo Uniforme")
    teste_custouniforme()
    print("\n---------------------------------------\n")
    print("Profundidade Limitada")
    teste_profundidadelimitada()
    print("\n---------------------------------------\n")
    print("Procura Sofrega")
    teste_procurasofrega()
    print("\n---------------------------------------\n")
    print("A Estrela")
    teste_aestrela()


def teste_procurasofrega():
    search = ProcuraSofrega("Coimbra", "Faro")
    resultado, x = search.algoritmo()
    print(resultado, x)
    #resultado.display()


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