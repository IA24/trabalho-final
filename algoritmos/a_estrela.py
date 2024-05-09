import heapq
from algoritmos.algoritmos import Algoritmos
from data import PAISES
from algoritmos.resultado import Resultado


class AEstrela(Algoritmos):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)

    def algoritmo(self):
        open_list = [(0, self.origem)] #lista de prioridades
        came_from = {} #diconario no por onde já passou
        g_score = {self.origem: 0} #diconario custo para chegar ao no desde o inicio

        while open_list: #enquanto existirem nos dentro da lista continua
            current_cost, current_node = heapq.heappop(open_list) #para isso tira o no com o menor custo e compara
            if current_node == self.destino: #se o no for o destino
                path = [current_node]
                while current_node in came_from:
                    current_node = came_from[current_node]
                    path.append(current_node)
                path.reverse()
                resultado = Resultado(path, self.origem, self.destino) #guarda o caminho pelo codigo que passou
                return resultado

            for neighbor in self.conexoes.conexao[current_node]:
                tentative_g_score = g_score[current_node] + self.conexoes.conexao[current_node][neighbor] # para o proximo no calcula um custo imaginario somando o custo já percorrido até o nó atual com o custo que leva ao vizinho.
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]: # se o custo imaginario for menor do que o custo para chegar ao vizinho ou ainda n foi visitado
                    came_from[neighbor] = current_node #define o no atual como o no anterior
                    g_score[neighbor] = tentative_g_score #atualiza o custo para chegar ao vizinho
                    heuristica = PAISES.calcular_distancia_reta(neighbor, self.destino) #calcula a distancia do no vizinho até ao destino
                    f_score = tentative_g_score + heuristica #calcula o valor f para o vizinho
                    heapq.heappush(open_list, (f_score, neighbor)) #adiciona o vizinho na lista com a prioridade f
        return None
