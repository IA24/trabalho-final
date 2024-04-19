import math


class Pais:
    def __init__(self, nome, localizacoes):
        self.nome = nome
        self.localizacoes = localizacoes
        self.conexoes = []

    def obter_nome(self):
        return self.nome

    def obter_localizacoes(self):
        return self.localizacoes

    def obter_localizacao_by_nome(self, nome):
        for localizacao in self.localizacoes:
            if localizacao.nome.lower() == nome.lower():
                return localizacao
        print(nome, "não existe.")
        return None

    def localizacao_existe(self, nome):
        if self.obter_localizacao_by_nome(nome):
            return True
        else:
            return False

    def calcular_distancia(self, local1, local2):
        distancia = math.sqrt((local1.longitude - local2.longitude) ** 2 + (local2.latitude - local1.latitude) ** 2)

        return int(distancia * 100)

    def display(self):
        i = 1
        print(self.nome)
        for local in self.localizacoes:
            print("\n" + str(i) + ".")
            local.display()
            i += 1

    def set_conexoes(self, conexoes):
        self.conexoes = conexoes

    def set_localizacoes(self, localizacoes):
        self.localizacoes = localizacoes

    def cidades_conectadas(self, localizacao):
        conexoes_por_localizacao = {}
        for conexao in self.conexoes:
            if conexao.localizacao1 == localizacao:
                if localizacao in conexoes_por_localizacao:
                    conexoes_por_localizacao[localizacao].append(conexao.localizacao2)
                else:
                    conexoes_por_localizacao[localizacao] = [conexao.localizacao2]
            elif conexao.localizacao2 == localizacao:
                if localizacao in conexoes_por_localizacao:
                    conexoes_por_localizacao[localizacao].append(conexao.localizacao1)
                else:
                    conexoes_por_localizacao[localizacao] = [conexao.localizacao1]

        return conexoes_por_localizacao

