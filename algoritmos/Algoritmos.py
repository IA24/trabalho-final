from data import PAISES, CONEXOES
from abc import ABC, abstractmethod
import heapq


class Algoritmos(ABC):
    def __init__(self, origem, destino):
        if not (CONEXOES and origem and destino):
            raise ValueError("Conexões, origem e destino devem ser fornecidos.")
        self.conexoes = CONEXOES
        self.origem = PAISES.obter_localizacao_by_nome(origem)
        self.destino = PAISES.obter_localizacao_by_nome(destino)

    def algoritmo(self):
        pass

    def display(self, resultado):
       pass