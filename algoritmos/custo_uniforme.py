from algoritmos.algoritmos import Algoritmos
from algoritmos.resultado import Resultado
import heapq

from data import PAISES


class CustoUniforme(Algoritmos):
    def algoritmo(self):
        custos = {self.origem: 0}
        predecessores = {self.origem: None}  # Dicionário para armazenar os predecessores
        explorados = set()
        fronteira = [(0, self.origem)]

        while fronteira:
            custo_atual, no_atual = heapq.heappop(fronteira)
            if no_atual in explorados: continue
            if no_atual == self.destino:
                # Construir e retornar o caminho percorrido
                caminho = []
                resultado = None
                while no_atual is not None:
                    caminho.insert(0, no_atual)
                    no_atual = predecessores[no_atual]
                    resultado = Resultado(caminho, self.origem, self.destino)
                return resultado
            explorados.add(no_atual)
            for neighbor in self.conexoes.conexao[no_atual]:
                distancia = self.conexoes.conexao[no_atual][neighbor]
                custo_acumulado = custo_atual + distancia
                if neighbor not in explorados and (neighbor not in custos or custo_acumulado < custos[neighbor]):
                    custos[neighbor] = custo_acumulado
                    predecessores[neighbor] = no_atual  # Atualiza o predecessor
                    heapq.heappush(fronteira, (custo_acumulado, neighbor))
        return None
