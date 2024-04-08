import heapq


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
        # Heurística simples: estimar a distância entre as cidades com base na tabela fornecida
        heuristic_table = {
            "Aveiro": 366, "Braga": 454, "Bragança": 487,
            "Beja": 99, "Castelo Branco": 280, "Coimbra": 319,
            "Évora": 157, "Faro": 0, "Guarda": 352,
            "Leiria": 278, "Lisboa": 195, "Portalegre": 228,
            "Porto": 418, "Santarém": 231, "Setúbal": 168,
            "Viana do Castelo": 473, "Vila Real": 429, "Viseu": 363, "Mangualde": 20
        }
        return heuristic_table[city]


def a_star_search(graph, start, goal):
    open_list = [(0, start)]  # Fila de prioridade para os nós a serem explorados
    came_from = {}  # Dicionário para armazenar os nós predecessores
    g_score = {start: 0}  # Dicionário para armazenar o custo do caminho do início até o nó atual

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path

        for neighbor in graph.edges[current_node]:
            tentative_g_score = g_score[current_node] + graph.edges[current_node][neighbor]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + graph.heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None


# Criando um grafo de exemplo
graph = Graph()

# Adicionando as conexões entre as cidades e suas distâncias
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

# Adicione mais conexões conforme necessário

# Executando a busca A*
start = "Santarém"
goal = "Faro"
path = a_star_search(graph, start, goal)

# Exibindo o caminho encontrado
if path:
    print("Caminho encontrado:")
    for city in path:
        print(city)
else:
    print("Caminho não encontrado.")
