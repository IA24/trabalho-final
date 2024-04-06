from algoritmos.custo_uniforme import SearchAlgorithms
from data import conexoes


def main():
    search = SearchAlgorithms(conexoes, "Aveiro", "Évora")
    resultado = search.custo_uniforme()
    search.display(resultado)


main()
