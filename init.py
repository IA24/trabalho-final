from localizacao.localizacao import Localizacao
from localizacao.pais import Pais
from localizacao.conexoes import Conexoes


def cria_conexoes(pais):
    conexoes = []
    with open("files/conexoes.txt", 'r', encoding='utf-8') as file:
        for line in file:
            string = line.strip().split('; ')
            localizacao1, localizacao2, distancia = str(string[0]), str(string[1]), int(string[2])
            if localizacao1 and localizacao2 and distancia:
                con = Conexoes(pais.obter_localizacao_by_nome(localizacao1),
                               pais.obter_localizacao_by_nome(localizacao2), distancia)
                conexoes.append(con)
    return conexoes


def criar_localizacoes():
    localizacoes = []
    with open("files/localizacoes.txt", 'r', encoding='utf-8') as file:
        for line in file:
            string = line.strip().split('; ')
            nome, latitude, longitude = str(string[0]), float(string[1]), float(string[2])
            if nome and latitude and longitude:
                loc = Localizacao(nome, latitude, longitude)
                localizacoes.append(loc)
    return localizacoes


def init():
    localizacoes = criar_localizacoes()
    pais = Pais("Portugal", localizacoes)
    conexoes = cria_conexoes(pais)
    return conexoes, localizacoes, pais
