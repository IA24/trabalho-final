from data import PAISES, CONEXOES
from abc import ABC, abstractmethod
import heapq


class Algoritmos(ABC):
    def __init__(self, origem, destino):
        if CONEXOES is None or origem is None or destino is None:
            raise ValueError("Conexões, origem e destino devem ser fornecidos.")
        self.conexoes = CONEXOES
        self.origem = PAISES.obter_localizacao_by_nome(origem)
        self.destino = PAISES.obter_localizacao_by_nome(destino)

    @abstractmethod
    def algoritmo(self):
        pass
