from algoritmos.profundidade_limitada import ProfundidadeLimitada
from algoritmos.procura_sofrega import ProcuraSofrega
from algoritmos.a_estrela import AEstrela
from algoritmos.custo_uniforme import CustoUniforme


def teste():
    print("Profundidade Limitada")
    teste_profundidadelimitada()
    print("\n---------------------------------------\n")
    print("Procura Sofrega")
    teste_procurasofrega()
    print("\n---------------------------------------\n")
    print("Custo Uniforme")
    teste_custouniforme()
    print("\n---------------------------------------\n")
    print("A Estrela")
    teste_aestrela()
    print("\n---------------------------------------\n")


def calcular_distancia_total(caminho, distancias):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        distancia_total += distancias[cidade_atual][proxima_cidade]
    return distancia_total


def teste_procurasofrega():
    search = ProcuraSofrega("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


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
