from algoritmos.algoritmos import Algoritmos
import heapq


class ProcuraSofrega(Algoritmos):
    def algoritmo(self):
        fila_prioridade = [(0, self.origem, [])]
        visitados = set()
        while fila_prioridade:
            custo_atual, localizacao_atual, caminho_atual = heapq.heappop(fila_prioridade)
            if localizacao_atual in visitados:
                continue
            visitados.add(localizacao_atual)
            if localizacao_atual == self.destino:
                return custo_atual, caminho_atual + [localizacao_atual], self.origem, self.destino
            for conexao in self.conexoes:
                if conexao.localizacao1 == localizacao_atual:
                    nova_localizacao = conexao.localizacao2
                elif conexao.localizacao2 == localizacao_atual:
                    nova_localizacao = conexao.localizacao1
                else:
                    continue
                if nova_localizacao not in visitados:
                    novo_custo = custo_atual + conexao.heuristica
                    novo_caminho = caminho_atual + [localizacao_atual]
                    heapq.heappush(fila_prioridade, (novo_custo, nova_localizacao, novo_caminho))
        return float('inf'), [], self.origem, self.destino
