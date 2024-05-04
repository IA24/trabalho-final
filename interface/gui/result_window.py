import tkinter as tk
import random

from interface.gui.mapa_window import MapaWindow


class ResultWindow(tk.Toplevel):
    def __init__(self, parent, result, window_title):
        super().__init__(parent)
        self.title(window_title)
        self.result = result
        self.create_widgets()

    def create_widgets(self):
        row = 0
        self.create_input_with_label("Origem", self.result.obter_origem(), row)
        row = row + 1
        self.create_input_with_label("Destino", self.result.obter_destino(), row)
        row = row + 1
        if self.result.obter_profundiade() != float("inf"):
            self.create_input_with_label("Profundidade", self.result.obter_profundiade(), row)
            row = row + 1
        self.create_input_with_label("Distância", self.result.obter_distancia(), row)
        row = row + 1
        self.create_input_with_label("Distância (linha reta)", self.result.obter_distancia_reta(), row)
        row = row + 1
        self.create_input_with_label("Caminho", self.result.obter_caminho(), row)
        button_row = row + 1
        button = tk.Button(self, text="Ver caminho", command=self.open_map)  # Cria o botão
        button.grid(row=button_row, column=0, pady=10)  # Posiciona o botão na janela

    def create_input_with_label(self, label_text, content, row=0):
        label = tk.Label(self, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5)
        input_field = tk.Entry(self, state="disabled")
        input_field.grid(row=row, column=1, padx=5, pady=5)
        input_field.configure(state="normal")
        input_field.insert(tk.END, content) if content is not None else None
        input_field.configure(state="disabled")

    def open_map(self):
        # Gera coordenadas aleatórias para o mapa
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Abre a janela do mapa com as coordenadas aleatórias
        MapaWindow(self, latitude, longitude)
