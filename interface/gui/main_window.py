import tkinter as tk
from tkinter import simpledialog
from algoritmos.custo_uniforme import CustoUniforme
from algoritmos.profundidade_limitada import ProfundidadeLimitada
from algoritmos.a_estrela import AEstrela
from data import PAISES
from algoritmos.procura_sofrega import ProcuraSofrega
from interface.gui.result_window import ResultWindow
from interface.interface import Interface


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métodos de Procura")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Escolha um algoritmo:", font=('Arial', 14)).pack(pady=10)  # Criação da label

        options = [("Custo Uniforme", 1), ("Profundidade Limitada", 2),
                   ("Procura Sôfrega", 3), ("A*", 4)]  # Intanciação dos botões

        for text, algo_id in options:  # Criação dos botões
            tk.Button(self, text=text, width=20, height=2,
                      command=lambda id=algo_id: self.run_algorithm(id)).pack()

    def run_algorithm(self, algorithm_id):
        origem, destino, profundidade = self.get_inputs(algorithm_id)

        if origem is None or destino is None:
            return
        if algorithm_id == 2 and profundidade is float("inf"):
            return

        result_window_title = "Resultado | "
        result = None

        if algorithm_id == 1:
            result = Interface.custo_uniforme(origem, destino)
            result_window_title += "Custo Uniforme"
        elif algorithm_id == 2:
            result = Interface.profundidade_limitada(origem, destino, profundidade)
            result_window_title += "Profundidade Limitada"
        elif algorithm_id == 3:
            result = Interface.procura_sofrega(origem, destino)
            result_window_title += "Procura Sofrega"
        elif algorithm_id == 4:
            result = Interface.a_estrela(origem, destino)
            result_window_title += "A*"

        ResultWindow(self, result, result_window_title)  # Mostra a janela de resultados

    def get_inputs(self, algorithm_id):
        while True:
            origem = self.prompt_input("Origem:")
            if origem is None:
                return None, None, float("inf")
            if isinstance(origem, str) and PAISES.localizacao_existe(origem):
                break

        while True:
            destino = self.prompt_input("Destino:")
            if destino is None:
                return None, None, float("inf")
            if isinstance(destino, str) and PAISES.localizacao_existe(destino):
                break

        profundidade = float("inf")

        if algorithm_id == 2:
            while True:
                profundidade = self.prompt_input("Profundidade:")
                if profundidade is None:
                    return None, None, float("inf")
                try:
                    if profundidade is None:
                        return None, None, float("inf")
                    profundidade = int(profundidade)
                    break
                except ValueError:
                    pass

        return origem, destino, profundidade

    def prompt_input(self, prompt):
        return simpledialog.askstring(title="Input", prompt=prompt, parent=self)

    @staticmethod
    def custo_uniforme(origem, destino):
        search = CustoUniforme(origem, destino)
        return search.algoritmo()

    @staticmethod
    def a_estrela(origem, destino):
        search = AEstrela(origem, destino)
        return search.algoritmo()

    @staticmethod
    def procura_sofrega(origem, destino):
        search = ProcuraSofrega(origem, destino)
        return search.algoritmo()

    @staticmethod
    def profundidade_limitada(origem, destino, profundidade):
        search = ProfundidadeLimitada(origem, destino, profundidade)
        return search.algoritmo()
