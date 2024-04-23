from localizacao.localizacao import Localizacao
from localizacao.pais import Pais
from localizacao.conexoes import Conexoes
from localizacao.conexoes_faro import ConexoesFaro
from utils import Utils


def cria_conexoes(pais):
    with open("files/conexoes.txt", 'r', encoding='utf-8') as file:
        conexoes = Conexoes()
        for line in file:
            string = line.strip().split('; ')
            localizacao1, localizacao2, distancia = str(string[0]), str(string[1]), int(string[2])
            if localizacao1 and localizacao2 and distancia:
                conexao = conexoes.add_conexao(pais.obter_localizacao_by_nome(localizacao1),
                                             pais.obter_localizacao_by_nome(localizacao2), distancia)
    return conexoes


def cria_conexoes_faro(pais):
    conexoes_faro = []
    with open("files/conexoes_faro.txt", 'r', encoding='utf-8') as file:
        for line in file:
            string = line.strip().split('; ')
            localizacao, distancia = str(string[0]), int(string[1])
            if localizacao and distancia:
                conexao = ConexoesFaro(pais.obter_localizacao_by_nome(localizacao), pais.obter_localizacao_by_nome("Faro"), distancia)
                conexoes_faro.append(conexao)
    return conexoes_faro


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
    Utils.limpar_consola()
    localizacoes = criar_localizacoes()
    pais = Pais("Portugal", localizacoes)
    conexoes = cria_conexoes(pais)
    pais.set_conexoes(conexoes)
    conexoes_faro = cria_conexoes_faro(pais)
    pais.set_conexoes_faro(conexoes_faro)
    return conexoes, localizacoes, pais, conexoes_faro
