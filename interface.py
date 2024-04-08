from algoritmos.custo_uniforme import CustoUniforme
from data import pais
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
        try:
            if opcao == "exit":
                break
            elif int(opcao) in [0, 1, 2, 3, 4]:
                Utils.limpar_consola()
                origem, destino = interface_inputs()
                if int(opcao) == 1:
                    interface_custo_uniforme(origem, destino)
                elif int(opcao) == 2:
                    pass
                elif int(opcao) == 3:
                    pass
                elif int(opcao) == 4:
                    pass
        except ValueError as ve:
            print("Erro: A opção não é válida.")
            Utils.enter_to_continue()
            Utils.limpar_consola()
            continue


def interface_custo_uniforme(origem, destino):
    search = CustoUniforme(origem, destino)
    resultado = search.algoritmo()
    search.display(resultado)
    Utils.enter_to_continue()
    Utils.limpar_consola()


def interface_inputs():
    while True:
        origem = input("Origem: ")
        if isinstance(origem, str) and pais.localizacao_existe(origem):
            break
    while True:
        destino = input("Destino: ")
        if isinstance(destino, str) and pais.localizacao_existe(destino):
            break
    return origem, destino
