from data import PAISES, CONEXOES


class Resultado:
    def __init__(self, caminho, origem, destino, profundidade=-1):
        self.origem = origem
        self.destino = destino
        self.caminho = caminho
        self.distancia = self.calcular_distancia()
        self.distancia_reta = PAISES.calcular_distancia_reta(origem, destino)
        if profundidade is not None:
            self.profundidade = profundidade
        else:
            self.profundidade = -1

    def display(self):
        print("Origem:", self.origem.obter_nome())
        print("Destino:", self.destino.obter_nome())
        if self.profundidade != -1:
            print("Profundidade:", self.profundidade)
        print("Distância:", self.distancia, "km")
        print("Distância (linha reta):", self.distancia_reta, "km")
        caminho_str = ""
        for i, item in enumerate(self.caminho):
            if i > 0:
                distancia = PAISES.calcular_distancia_reta(self.caminho[i - 1], item)
                caminho_str += " <" + str(distancia) + "> "
            caminho_str += item.obter_nome()
        print("Caminho percorrido:", caminho_str)

    def calcular_distancia(self):
        if self.caminho is None or len(self.caminho) < 2:
            return 0

        distancia_total = 0
        for i in range(len(self.caminho) - 1):
            cidade_atual = self.caminho[i]
            proxima_cidade = self.caminho[i + 1]
            distancia_total += CONEXOES.conexao[cidade_atual][proxima_cidade]

        return distancia_total
