class Pais:
    def __init__(self, nome, localizacoes):
        self.nome = nome
        self.localizacoes = localizacoes

    def obter_nome(self):
        return self.nome

    def obter_localizacoes(self):
        return self.localizacoes

    def obter_localizacao_nome(self, nome):
        for localizacao in self.localizacoes:
            if localizacao.nome == nome:
                return localizacao
        return None

    def display(self):
        print(self.nome)
        for local in self.localizacoes:
            local.display()

