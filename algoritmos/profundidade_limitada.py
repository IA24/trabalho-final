from algoritmos.algoritmos import Algoritmos
from algoritmos.resultado import Resultado
import heapq


class ProfundidadeLimitada(Algoritmos):
    def busca(self, origem, destino, nivel_maximo, caminho_atual=None):
        if caminho_atual is None:
            caminho_atual = []

        caminho_atual = caminho_atual + [origem]

        if origem == destino:
            return caminho_atual

        if len(caminho_atual) > nivel_maximo:
            return None

        for vizinha in self.conexoes.conexao[origem]:
            if vizinha not in caminho_atual:
                novo_caminho = self.busca(vizinha, destino, nivel_maximo, caminho_atual)
                if novo_caminho is not None:
                    return novo_caminho

        return None

    def algoritmo(self):
        novo_caminho = self.busca(self.origem, self.destino, self.profundidade)
        resultado = Resultado(novo_caminho, self.origem, self.destino, self.profundidade)
        return resultado
