from data import PAISES, CONEXOES
from localizacao.localizacao import Localizacao


class Resultado:
    def __init__(self, caminho, origem: Localizacao, destino: Localizacao, profundidade=float("inf")):
        self.origem = origem
        self.destino = destino
        self.caminho = caminho
        self.distancia = self.__calcular_distancia()
        self.distancia_reta = PAISES.calcular_distancia_reta(origem, destino)
        if profundidade is not None:
            self.profundidade = profundidade
        else:
            self.profundidade = -1

    def display(self):
        print(self.__str_origem())
        print(self.__str_destino())
        if self.profundidade != float("inf"):
            print(self.__str_profundidade())
        print(self.__str_distancia())
        print(self.__str_distancia_reta())
        print(self.__str_caminho())

    def obter(self):
        resultado = ""
        resultado += self.__str_origem()
        resultado += "\n"
        resultado += self.__str_destino()
        resultado += "\n"
        if self.profundidade != float("inf"):
            resultado += self.__str_profundidade()
            resultado += "\n"
        resultado += self.__str_distancia()
        resultado += "\n"
        resultado += self.__str_distancia_reta()
        resultado += "\n"
        resultado += self.__str_caminho()
        resultado += "\n"
        print(resultado)
        return resultado

    def __calcular_distancia(self):
        if self.caminho is None or len(self.caminho) < 2:
            return 0
        distancia_total = 0
        for i in range(len(self.caminho) - 1):
            cidade_atual = self.caminho[i]
            proxima_cidade = self.caminho[i + 1]
            distancia_total += CONEXOES.conexao[cidade_atual][proxima_cidade]
        return distancia_total

    def __str_origem(self):
        return "Origem: " + self.origem.obter_nome()

    def __str_destino(self):
        return "Destino: " + self.destino.obter_nome()

    def __str_profundidade(self):
        return "Profundidade: " + str(self.profundidade)

    def __str_distancia(self):
        return "Distância: " + str(self.distancia) + "km"

    def __str_distancia_reta(self):
        return "Distância (linha reta): " + str(self.distancia_reta) + "km"

    def __str_caminho(self):
        return "Caminho percorrido: " + self.obter_caminho_with_distance()

    def obter_caminho_with_distance(self):
        caminho_str = ""
        for i, item in enumerate(self.caminho):
            if i > 0:
                distancia = PAISES.calcular_distancia_reta(self.caminho[i - 1], item)
                caminho_str += " <" + str(distancia) + "> "
            caminho_str += item.obter_nome()
        return caminho_str

    def obter_caminho(self):
        return self.caminho

    def obter_origem(self):
        return self.origem

    def obter_destino(self):
        return self.destino

    def obter_profundiade(self):
        return self.profundidade

    def obter_distancia(self):
        return self.distancia

    def obter_distancia_reta(self):
        return self.distancia_reta
