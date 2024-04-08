from algoritmos.Algoritmos import Algoritmos
import heapq

from data import PAISES


class CustoUniforme(Algoritmos):
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
                    novo_custo = custo_atual + conexao.distancia
                    novo_caminho = caminho_atual + [localizacao_atual]
                    heapq.heappush(fila_prioridade, (novo_custo, nova_localizacao, novo_caminho))
        return float('inf'), [], self.origem, self.destino

    def display(self, resultado):
        custo, caminho, origem, destino = resultado
        if custo == float('inf'):
            print("Não foi encontrado um caminho entre", origem, "e", destino)
            return
        print("Origem:", origem.obter_nome())
        print("Destino:", destino.obter_nome())
        print("Custo:", custo, "km")
        print("Custo em linha reta", PAISES.calcular_distancia(caminho[0], caminho[-1]), "km")
        caminho_str = ""
        distancia = ""
        for i, item in enumerate(caminho):
            if i > 0:
                distancia = PAISES.calcular_distancia(caminho[i - 1], item)
                caminho_str += " <" + str(distancia) + "> "
            caminho_str += item.obter_nome()
        print("Caminho percorrido:", caminho_str)
