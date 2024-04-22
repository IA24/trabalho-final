from data import PAISES


class Result:
    def __init__(self, caminho, distancia, origem, destino):
        self.origem = origem
        self.destino = destino
        self.caminho = caminho
        self.distancia = distancia
        self.distancia_reta = PAISES.calcular_distancia_reta(origem, destino)

    def display(self):
        print("Origem:", self.origem.obter_nome())
        print("Destino:", self.destino.obter_nome())
        print("Distância:", self.distancia, "km")
        print("Distância (linha reta):", self.distancia_reta, "km")
        caminho_str = ""
        for i, item in enumerate(self.caminho):
            if i > 0:
                distancia = PAISES.calcular_distancia_reta(self.caminho[i - 1], item)
                caminho_str += " <" + str(distancia) + "> "
            caminho_str += item.obter_nome()
        print("Caminho percorrido:", caminho_str)

"""
caminho_str = None
for i, item in enumerate(caminho):
    if i > 0:
        distancia = PAISES.calcular_distancia_reta(caminho[i - 1], item)

        caminho_str += " <" + str(distancia) + "> "
    caminho_str += item.obter_nome()
print("Caminho percorrido:", caminho_str)
custo, caminho, origem, destino = resultado
if custo == float('inf'):
    print("Não foi encontrado um caminho entre", origem, "e", destino)
    return
print("Origem:", origem.obter_nome())
print("Destino:", destino.obter_nome())
print("Custo:", custo, "km")
print("Custo em linha reta", PAISES.calcular_distancia_reta(caminho[0], caminho[-1]), "km")
caminho_str = ""
distancia = ""
for i, item in enumerate(caminho):
    if i > 0:
        distancia = PAISES.calcular_distancia_reta(caminho[i - 1], item)
        caminho_str += " <" + str(distancia) + "> "
    caminho_str += item.obter_nome()
print("Caminho percorrido:", caminho_str)"""