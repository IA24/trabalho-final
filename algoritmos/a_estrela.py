import heapq
from algoritmos.algoritmos import Algoritmos
from data import PAISES
from algoritmos.resultado import Resultado


class AEstrela(Algoritmos):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)

    def algoritmo(self):
        open_list = [(0, self.origem)]
        came_from = {}
        g_score = {self.origem: 0}

        while open_list:
            current_cost, current_node = heapq.heappop(open_list)
            if current_node == self.destino:
                path = [current_node]
                while current_node in came_from:
                    current_node = came_from[current_node]
                    path.append(current_node)
                path.reverse()
                resultado = Resultado(path, self.origem, self.destino)
                return resultado

            for neighbor in self.conexoes.conexao[current_node]:
                tentative_g_score = g_score[current_node] + self.conexoes.conexao[current_node][neighbor]
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    heuristica = PAISES.calcular_distancia_reta(neighbor, self.destino)
                    f_score = tentative_g_score + heuristica
                    heapq.heappush(open_list, (f_score, neighbor))
        return None
