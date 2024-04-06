class Conexoes:
    def __init__(self, localizacao1, localizacao2, distancia):
        self.localizacao1 = localizacao1
        self.localizacao2 = localizacao2
        self.distancia = distancia

    def display(self):
        print(str(self.localizacao1.obter_nome()) + ", " + str(self.localizacao2.obter_nome()) + ", " + str(self.distancia))