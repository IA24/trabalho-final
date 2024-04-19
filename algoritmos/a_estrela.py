from algoritmos.Algoritmos import Algoritmos
from algoritmos.a_estrela_old import Graph, a_star_search
from data import CONEXOES


class AEstrela(Algoritmos):

    graph = Graph()

    for conexao in CONEXOES:
        localizacao1 = conexao.localizacao1.nome
        localizacao2 = conexao.localizacao2.nome
        distancia = conexao.distancia
        graph.add_edge(localizacao1, localizacao2, distancia)

    start = "Coimbra"
    goal = "Faro"
    path, total_cost = a_star_search(graph, start, goal)

    # Displaying the found path and total cost
    if path:
        print("Caminho encontrado:")
        for city in path:
            print(city)
        print("Custo total da distância:", total_cost)
    else:
        print("Caminho não encontrado.")
