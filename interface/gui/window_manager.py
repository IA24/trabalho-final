from interface.gui.main_window import MainWindow
from interface.gui.mapa_window import MapaWindow
from interface.gui.result_window import ResultWindow
import tkinter as tk


class WindowsManager:
    def __init__(self):
        self.root = tk.Tk()
        self.result_window = None

    def open_main_window(self):
        main_window = MainWindow()
        main_window.mainloop()

    def open_result_window(self, result, title):
        if self.result_window:
            self.result_window.destroy()
        self.result_window = ResultWindow(self.root, result, title)

    def open_map_window(self, latitude, longitude):
        MapaWindow(self.root, latitude, longitude)
