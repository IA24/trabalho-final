import heapq
from data import PAISES

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, city1, city2, distance):
        if city1 not in self.edges:
            self.edges[city1] = {}
        if city2 not in self.edges:
            self.edges[city2] = {}
        self.edges[city1][city2] = distance
        self.edges[city2][city1] = distance

    def get_distance(self, city1, city2):
        return self.edges[city1][city2]

    def get_neighbors(self, city):
        return self.edges[city]

    def heuristic(self, city, goal):
        localizacao1 = PAISES.obter_localizacao_by_nome(city)
        localizacao2 = PAISES.obter_localizacao_by_nome(goal)

        distanciaheuristica = PAISES.calcular_distancia(localizacao1,localizacao2)
        return distanciaheuristica


def a_star_search(graph, start, goal):
    open_list = [(0, start)]  # Priority queue for nodes to be explored
    came_from = {}  # Dictionary to store predecessor nodes
    g_score = {start: 0}  # Dictionary to store cost of path from start to current node

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            total_cost = sum(graph.get_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            return path, total_cost

        for neighbor in graph.edges[current_node]:
            tentative_g_score = g_score[current_node] + graph.edges[current_node][neighbor]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + graph.heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None, None

# Creating an example graph
graph = Graph()

# Adding connections between cities and their distances
graph.add_edge("Aveiro", "Porto", 68)
graph.add_edge("Aveiro", "Viseu", 95)
graph.add_edge("Aveiro", "Coimbra", 68)
graph.add_edge("Aveiro", "Leiria", 115)
graph.add_edge("Braga", "Viana do Castelo", 48)
graph.add_edge("Braga", "Vila Real", 106)
graph.add_edge("Braga", "Porto", 53)
graph.add_edge("Bragança", "Vila Real", 137)
graph.add_edge("Bragança", "Guarda", 202)
graph.add_edge("Beja", "Évora", 78)
graph.add_edge("Beja", "Faro", 152)
graph.add_edge("Beja", "Setúbal", 142)
graph.add_edge("Castelo Branco", "Coimbra", 159)
graph.add_edge("Castelo Branco", "Guarda", 106)
graph.add_edge("Castelo Branco", "Portalegre", 80)
graph.add_edge("Castelo Branco", "Évora", 203)
graph.add_edge("Coimbra", "Viseu", 96)
graph.add_edge("Coimbra", "Leiria", 67)
graph.add_edge("Évora", "Lisboa", 150)
graph.add_edge("Évora", "Santarém", 117)
graph.add_edge("Évora", "Portalegre", 131)
graph.add_edge("Évora", "Setúbal", 103)
graph.add_edge("Faro", "Setúbal", 249)
graph.add_edge("Faro", "Lisboa", 299)
graph.add_edge("Guarda", "Vila Real", 157)
graph.add_edge("Guarda", "Viseu", 85)
graph.add_edge("Leiria", "Lisboa", 129)
graph.add_edge("Leiria", "Santarém", 70)
graph.add_edge("Lisboa", "Santarém", 78)
graph.add_edge("Lisboa", "Setúbal", 50)
graph.add_edge("Porto", "Viana do Castelo", 71)
graph.add_edge("Porto", "Vila Real", 116)
graph.add_edge("Porto", "Viseu", 133)
graph.add_edge("Vila Real", "Viseu", 110)

# Add more connections as needed

# Running A* search
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
