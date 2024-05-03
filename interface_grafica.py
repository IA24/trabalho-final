import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
from io import StringIO
from algoritmos.custo_uniforme import CustoUniforme
from algoritmos.profundidade_limitada import ProfundidadeLimitada
from algoritmos.a_estrela import AEstrela
from data import PAISES
from algoritmos.procura_sofrega import ProcuraSofrega

class PrintRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.buffer = StringIO()

    def write(self, text):
        self.buffer.write(text)
        self.flush()

    def flush(self):
        output = self.buffer.getvalue()
        if output:
            self.text_widget.insert(tk.END, output)
            self.text_widget.see(tk.END)
            self.buffer.truncate(0)
            self.buffer.seek(0)

class GUIInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Gráfica")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Escolha um algoritmo:", font=('Arial', 14)).pack(pady=10)

        options = [("Custo Uniforme", 1), ("Profundidade Limitada", 2),
                   ("Procura Sôfrega", 3), ("A*", 4)]

        for text, algo_id in options:
            tk.Button(self, text=text, width=20, height=2,
                      command=lambda id=algo_id: self.run_algorithm(id)).pack()

        self.result_text = tk.Text(self, height=10, width=50, wrap=tk.WORD)
        self.result_text.pack(pady=20)

        self.print_redirector = PrintRedirector(self.result_text)
        sys.stdout = self.print_redirector

    def run_algorithm(self, algorithm_id):
        origem, destino, profundidade = self.get_inputs(algorithm_id)

        if algorithm_id == 1:
            result = self.custo_uniforme(origem, destino)
        elif algorithm_id == 2:
            result = self.profundidade_limitada(origem, destino, profundidade)
        elif algorithm_id == 3:
            result = self.procura_sofrega(origem, destino)
        elif algorithm_id == 4:
            result = self.a_estrela(origem, destino)

        self.result_text.delete('1.0', tk.END)

        if result:
            result.display()  # Chama o método display() do objeto Resultado
        else:
            self.result_text.insert(tk.END, "Nenhum resultado encontrado.")

    def custo_uniforme(self, origem, destino):
        search = CustoUniforme(origem, destino)
        return search.algoritmo()

    def a_estrela(self, origem, destino):
        search = AEstrela(origem, destino)
        return search.algoritmo()

    def procura_sofrega(self, origem, destino):
        search = ProcuraSofrega(origem, destino)
        return search.algoritmo()

    def profundidade_limitada(self, origem, destino, profundidade):
        search = ProfundidadeLimitada(origem, destino, profundidade)
        return search.algoritmo()

    def get_inputs(self, algorithm_id):
        while True:
            origem = self.prompt_input("Origem:")
            if isinstance(origem, str) and PAISES.localizacao_existe(origem):
                break

        while True:
            destino = self.prompt_input("Destino:")
            if isinstance(destino, str) and PAISES.localizacao_existe(destino):
                break

        profundidade = -1

        if algorithm_id == 2:
            while True:
                profundidade = self.prompt_input("Profundidade:")
                try:
                    profundidade = int(profundidade)
                    break
                except ValueError:
                    pass

        return origem, destino, profundidade

    def prompt_input(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self)

def main():
    app = GUIInterface()
    app.mainloop()

if __name__ == "__main__":
    main()
