class Localizacao:
    def __init__(self, nome, latitude, longitude):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        if isinstance(other, Localizacao):
            return self.nome == other.nome
        return False

    def __hash__(self):
        return hash(self.nome)

    def __lt__(self, other):
        # Para fins de exemplo, vamos comparar as localizações com base no nome
        return self.nome < other.nome

    def __str__(self):
        return self.nome

    def obter_nome(self):
        return self.nome

    def obter_latitude(self):
        return self.latitude

    def obter_longitude(self):
        return self.longitude

    def display(self):
        print(self.nome + "\n" + str(self.latitude) + ", " + str(self.longitude))
