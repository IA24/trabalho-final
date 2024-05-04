import math


class Pais:
    def __init__(self, nome, localizacoes):
        self.nome = nome
        self.localizacoes = localizacoes
        self.conexoes = []
        self.conexoes_faro = []

    def obter_nome(self):
        return self.nome

    def obter_localizacoes(self):
        return self.localizacoes

    def obter_localizacao_by_nome(self, nome):
        if not isinstance(nome, str):
            return

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

    def calcular_distancia_reta(self, local1, local2):
        if local1 is None or local2 is None:
            return -1
        if local1 == local2:
            return 0
        faro = self.obter_localizacao_by_nome("Faro")
        if local1 == faro:
            conexao = self.__busca_conexoes_faro(local2)
            return conexao.distancia
        elif local2 == faro:
            conexao = self.__busca_conexoes_faro(local1)
            return conexao.distancia
        else:
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

    def set_conexoes_faro(self, conexoes_faro):
        self.conexoes_faro = conexoes_faro

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

    def __busca_conexoes_faro(self, local):
        for conexao in self.conexoes_faro:
            if conexao.localizacao == local:
                return conexao
