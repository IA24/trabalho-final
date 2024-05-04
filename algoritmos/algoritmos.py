from data import PAISES, CONEXOES
from abc import ABC, abstractmethod
from localizacao.localizacao import Localizacao
import heapq


class Algoritmos(ABC):
    def __init__(self, origem: Localizacao, destino: Localizacao, profundidade=0):
        if CONEXOES is None or origem is None or destino is None:
            raise ValueError("Conexões, origem e destino devem ser fornecidos.")
        self.conexoes = CONEXOES
        self.origem = PAISES.obter_localizacao_by_nome(origem)
        self.destino = PAISES.obter_localizacao_by_nome(destino)
        self.profundidade = profundidade

    @abstractmethod
    def algoritmo(self):
        pass
