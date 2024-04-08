from algoritmos.a_estrela import AEstrela
from algoritmos.procura_sofrega import ProcuraSofrega
from algoritmos.custo_uniforme import CustoUniforme
from algoritmos.profundidade_limitada import ProfundidadeLimitada
from data import PAISES
from utils import Utils


class Interface:
    @staticmethod
    def interface():
        while True:
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
                    origem, destino = Interface.inputs()
                    if int(opcao) == 1:
                        Interface.custo_uniforme(origem, destino)
                    elif int(opcao) == 2:
                        Interface.profundidade_limitada(origem, destino)
                    elif int(opcao) == 3:
                        Interface.procura_sofrega(origem, destino)
                    elif int(opcao) == 4:
                        Interface.a_estrela(origem, destino)
            except ValueError as ve:
                print("Erro: A opção não é válida.")
                Utils.enter_to_continue()
                Utils.limpar_consola()
                continue

    @staticmethod
    def custo_uniforme(origem, destino):
        search = CustoUniforme(origem, destino)
        resultado = search.algoritmo()
        search.display(resultado)
        Utils.enter_to_continue()
        Utils.limpar_consola()

    @staticmethod
    def a_estrela(origem, destino):
        search = AEstrela(origem, destino)
        resultado = search.algoritmo()
        search.display(resultado)
        Utils.enter_to_continue()
        Utils.limpar_consola()

    @staticmethod
    def procura_sofrega(origem, destino):
        search = ProcuraSofrega(origem, destino)
        resultado = search.algoritmo()
        search.display(resultado)
        Utils.enter_to_continue()
        Utils.limpar_consola()

    @staticmethod
    def profundidade_limitada(origem, destino):
        search = ProfundidadeLimitada(origem, destino)
        resultado = search.algoritmo()
        search.display(resultado)
        Utils.enter_to_continue()
        Utils.limpar_consola()

    @staticmethod
    def inputs():
        while True:
            origem = input("Origem: ")
            if isinstance(origem, str) and PAISES.localizacao_existe(origem):
                break
        while True:
            destino = input("Destino: ")
            if isinstance(destino, str) and PAISES.localizacao_existe(destino):
                break
        Utils.limpar_consola()
        return origem, destino
