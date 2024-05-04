import tkinter as tk
from tkinter import ttk
import folium
import webbrowser
import os


class MapaWindow(tk.Toplevel):
    def __init__(self, parent, latitude, longitude, window_title="Mapa"):
        super().__init__(parent)
        self.title(window_title)
        self.latitude = latitude
        self.longitude = longitude
        self.create_map()

    def create_map(self):
        map_frame = ttk.Frame(self)
        map_frame.pack(fill='both', expand=True)

        mapa = folium.Map(location=[self.latitude, self.longitude], zoom_start=15)
        folium.Marker([self.latitude, self.longitude], popup="Local", tooltip="Clique para mais informações").add_to(mapa)

        # Salva o mapa em um arquivo HTML temporário
        mapa.save("mapa_temp.html")

        # Carrega o mapa HTML em um navegador web embutido
        map_browser = ttk.Frame(map_frame)
        map_browser.pack(fill='both', expand=True)

        self.browser = webbrowser.MiniBrowser(master=map_browser)
        self.browser.pack(fill='both', expand=True)
        self.browser.open(url="file://" + os.path.abspath("mapa_temp.html"))

        # Exclui o arquivo HTML temporário ao fechar a janela
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Fecha a janela e exclui o arquivo HTML temporário
        self.destroy()
        os.remove("mapa_temp.html")
