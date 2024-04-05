class Mapa:
    def __init__(self, nome, coordenadas):
        self.nome = nome
        latitude_str, longitude_str = coordenadas.split(", ")
        self.latitude = float(latitude_str)
        self.longitude = float(longitude_str)

    def obter_nome(self):
        return self.nome

    def obter_latitude(self):
        return self.latitude

    def obter_longitude(self):
        return self.longitude

    def display(self):
        print(self.nome + "\n" + str(self.latitude) + ", " + str(self.longitude))
