from interface import Interface
from algoritmos.a_estrela import AEstrela
from data import CONEXOES, PAISES, LOCALIZACOES


def main():
    #Interface.interface()

    CONEXOES.display_all()

    teste_aestrela()


def teste_aestrela():
    search = AEstrela("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


main()




