from data import pais, conexoes
import heapq


class SearchAlgorithms:
    def __init__(self, origem, destino):
        if not (conexoes and origem and destino):
            raise ValueError("Conexões, origem e destino devem ser fornecidos.")
        self.conexoes = conexoes
        self.origem = pais.obter_localizacao_by_nome(origem)
        self.destino = pais.obter_localizacao_by_nome(destino)

    def custo_uniforme(self):
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
        print("Custo:", custo)
        caminho_str = ""
        for i, cam in enumerate(caminho):
            caminho_str += cam.obter_nome()
            if i < len(caminho) - 1:
                caminho_str += ", "
        print("Caminho percorrido:", caminho_str)
