from interface import Interface
from algoritmos.a_estrela import AEstrela


def main():
    #Interface.interface()

    teste_aestrela()


def teste_aestrela():
    search = AEstrela("Coimbra", "Faro")
    resultado = search.algoritmo()
    resultado.display()


main()




