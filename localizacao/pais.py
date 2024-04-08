import math

class Pais:
    def __init__(self, nome, localizacoes):
        self.nome = nome
        self.localizacoes = localizacoes

    def obter_nome(self):
        return self.nome

    def obter_localizacoes(self):
        return self.localizacoes

    def obter_localizacao_by_nome(self, nome):
        for localizacao in self.localizacoes:
            if localizacao.nome == nome:
                return localizacao
        print(nome, "não existe.")
        return None

    def localizacao_existe(self, nome):
        if self.obter_localizacao_by_nome(nome):
            return True
        else:
            return False

    def calcular_distancia(self, localizacao1, localizacao2):
        local1 = self.obter_localizacao_by_nome(localizacao1)
        local2 = self.obter_localizacao_by_nome(localizacao2)

        distancia = math.sqrt((local1.longitude - local2.longitude) ** 2 + (local2.latitude - local1.latitude) ** 2)

        return int(distancia * 100)

    def display(self):
        i = 1
        print(self.nome)
        for local in self.localizacoes:
            print("\n" + str(i) + ".")
            local.display()
            i += 1

