from data import pais, conexoes
from abc import ABC, abstractmethod
import heapq


class Algoritmos(ABC):
    def __init__(self, origem, destino):
        if not (conexoes and origem and destino):
            raise ValueError("Conexões, origem e destino devem ser fornecidos.")
        self.conexoes = conexoes
        self.origem = pais.obter_localizacao_by_nome(origem)
        self.destino = pais.obter_localizacao_by_nome(destino)

    def algoritmo(self):
        pass

    def display(self, resultado):
       pass