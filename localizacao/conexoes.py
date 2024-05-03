class Conexoes:
    def __init__(self):
        self.conexao = {}

    def add_conexao(self, localizacao1, localizacao2, distancia):
        if localizacao1 not in self.conexao:
            self.conexao[localizacao1] = {}
        if localizacao2 not in self.conexao:
            self.conexao[localizacao2] = {}
        self.conexao[localizacao1][localizacao2] = distancia
        self.conexao[localizacao2][localizacao1] = distancia

    def get_distance(self, localizacao1, localizacao2):
        if localizacao1 in self.conexao and localizacao2 in self.conexao[localizacao1]:
            return self.conexao[localizacao1][localizacao2]
        else:
            return float('inf')

    def get_neighbors(self, localizacao):
        return self.conexao[localizacao]

    def get_conexao(self, localizacao_string):
        for item in self.conexao:
            if item.nome == localizacao_string:
                return item
        return None

    def display_all(conexoes):
        for localizacao, conexoes in conexoes.conexao.items():
            print(f"{localizacao}: ", end="")
            conexoes_formatadas = []
            for destino, distancia in conexoes.items():
                conexoes_formatadas.append(f"{destino}: {distancia}")
            print("{ " + ", ".join(conexoes_formatadas) + " }")


