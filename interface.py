from data import pais
from algoritmos.SearchAlgorithms import SearchAlgorithms
from utils import Utils


def interface():
    is_running = True
    while is_running:
        print("0. Todos")
        print("1. Custo Uniforme")
        print("2. Profundidade Limitada")
        print("3. Procura Sôfrega")
        print("4. A*")
        opcao = input("Escolha um algoritmo: ")
        if int(opcao) in [0, 1, 2, 3, 4]:
            Utils.limpar_consola()
            while True:
                origem = input("Origem: ")
                if isinstance(origem, str) and pais.localizacao_existe(origem):
                    break
            while True:
                destino = input("Destino: ")
                if isinstance(destino, str) and pais.localizacao_existe(destino):
                    break
            if int(opcao) == 1:
                interface_custo_uniforme(origem, destino)
            elif int(opcao) == 2:
                pass
            elif int(opcao) == 3:
                pass
            elif int(opcao) == 4:
                pass


def interface_custo_uniforme(origem, destino):
    search = SearchAlgorithms(origem, destino)
    resultado = search.custo_uniforme()
    search.display(resultado)
    input("Pressione Enter para continuar...")
    Utils.limpar_consola()
