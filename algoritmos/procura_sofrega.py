import heapq
from algoritmos.algoritmos import Algoritmos
from algoritmos.resultado import Resultado
from data import CONEXOES, PAISES


class ProcuraSofrega (Algoritmos):
    def heuristica(self, cidade):
        if cidade in CONEXOES.conexao:
            return CONEXOES.get_distance(cidade, self.destino)
        return float('inf')

    def algoritmo(self):
        fila_prioridade = [(self.heuristica(self.origem), self.origem, [])]
        visitados = set()

        while fila_prioridade:
            _, localizacao_atual, caminho_atual = heapq.heappop(fila_prioridade)

            if localizacao_atual in visitados:
                continue

            visitados.add(localizacao_atual)

            if localizacao_atual == self.destino:
                resultado = Resultado(caminho_atual + [localizacao_atual], self.origem, self.destino)
                return resultado

            for nova_localizacao in CONEXOES.conexao[localizacao_atual]:
                if nova_localizacao not in visitados:
                    heapq.heappush(fila_prioridade, (
                        self.heuristica(nova_localizacao), nova_localizacao, caminho_atual + [localizacao_atual]))

        return []
