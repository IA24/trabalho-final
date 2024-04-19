from data import PAISES
from data import CONEXOES
from data import LOCALIZACOES
from init import init


distancias = {
    "Aveiro": {"Porto": 68, "Viseu": 95, "Coimbra": 68, "Leiria": 115},
    "Porto": {"Aveiro": 68, "Braga": 53, "Vila Real": 116},
    "Braga": {"Porto": 53, "Viana do Castelo": 48, "Vila Real": 137},
    "Viana do Castelo": {"Braga": 48, "Porto": 71},
    "Vila Real": {"Porto": 116, "Braga": 137, "Viseu": 110, "Guarda": 157},
    "Viseu": {"Aveiro": 95, "Porto": 133, "Coimbra": 96, "Guarda": 85, "Vila Real": 110},
    "Guarda": {"Bragança": 202, "Vila Real": 157, "Viseu": 85, "Castelo Branco": 106},
    "Bragança": {"Vila Real": 137, "Guarda": 202},
    "Coimbra": {"Aveiro": 68, "Viseu": 96, "Leiria": 67, "Castelo Branco": 159},
    "Leiria": {"Aveiro": 115, "Coimbra": 67, "Lisboa": 129, "Santarém": 70},
    "Castelo Branco": {"Coimbra": 159, "Guarda": 106, "Portalegre": 80, "Évora": 203},
    "Évora": {"Beja": 78, "Lisboa": 150, "Santarém": 117, "Setúbal": 103, "Portalegre": 131, "Castelo Branco": 203},
    "Beja": {"Évora": 78, "Faro": 152, "Setúbal": 142},
    "Faro": {"Beja": 152, "Setúbal": 249, "Lisboa": 299},
    "Setúbal": {"Évora": 103, "Beja": 142, "Lisboa": 50, "Faro": 249},
    "Lisboa": {"Leiria": 129, "Santarém": 78, "Setúbal": 50, "Évora": 150, "Faro": 299},
    "Santarém": {"Leiria": 70, "Lisboa": 78, "Évora": 117},
    "Portalegre": {"Castelo Branco": 80, "Évora": 131},
}


def busca_caminho_menor_custo(origem, destino, nivel_maximo, caminho_atual=[]):
    # Adiciona a cidade atual ao caminho atual
    caminho_atual = caminho_atual + [origem]

    # Se atingir o destino, retorna o caminho
    if origem == destino:
        return caminho_atual

    # Se atingir o nível máximo de profundidade, interrompe a busca nesse ramo
    if len(caminho_atual) > nivel_maximo:
        return None

    # Explora cada cidade vizinha
    for vizinha in distancias[origem]:
        if vizinha not in caminho_atual:  # Evita ciclos
            novo_caminho = busca_caminho_menor_custo(vizinha, destino, nivel_maximo, caminho_atual)
            if novo_caminho is not None:
                return novo_caminho

    return None


# Função principal para interagir com o usuário e chamar a busca
def encontrar_caminho():
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    nivel_maximo = int(input("Digite o nível máximo de profundidade: "))

    caminho = busca_caminho_menor_custo(origem, destino, nivel_maximo)

    if caminho is None:
        print("Não foi encontrado um caminho dentro do nível máximo de profundidade especificado.")
    else:
        print("Caminho encontrado:", caminho)
        print("Distância percorrida:", len(caminho) - 1)  # Distância é o número de cidades no caminho - 1


# Chamada da função principal
encontrar_caminho()


def profundidade_limitada(origem, destino, max_profundidade):
    stack = [(origem, [origem])]  # Pilha de nós a serem explorados, cada item é uma tupla (nó, caminho até o nó)

    while stack:
        (node, path) = stack.pop()  # Pegar o próximo nó e seu caminho

        if node == destino:
            return path  # Se chegamos ao destino, retornamos o caminho

        if len(path) < max_profundidade:  # Limita a busca à profundidade máxima
            for con in CONEXOES:
                if con.localizacao1 == node:
                    stack.append((con.localizacao2, path + [con.localizacao2]))

    return None

if __name__ == "__main__":
    CONEXOES, LOCALIZACOES, PAIS = init()

    origem = input("Insira a cidade de origem: ")
    destino = input("Insira a cidade de destino: ")
    max_profundidade = int(input("Insira o nível máximo de profundidade: "))

    origem_localizacao = PAIS.obter_localizacao_by_nome(origem)
    destino_localizacao = PAIS.obter_localizacao_by_nome(destino)

    if not origem_localizacao or not destino_localizacao:
        print("Localizações inválidas.")
    else:
        resultado = profundidade_limitada(origem_localizacao, destino_localizacao, max_profundidade)

        if resultado:
            print("Caminho encontrado:")
            for loc in resultado:
                print(loc.obter_nome())
            distancia_total = len(resultado) - 1  # A distância é o número de conexões no caminho
            print(f"Distância total do caminho: {distancia_total} conexões.")
        else:
            print("Caminho não encontrado até a profundidade especificada.")
