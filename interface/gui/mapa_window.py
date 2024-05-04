import webbrowser

import folium

from constants import TEMP_MAP_PATH
from data import LOCALIZACOES


class Mapa:
    def __init__(self, caminho):
        self.mapa = folium.Map(location=[39.670553299554, -8.008552309046332], zoom_start=7)
        self.caminho = caminho

    def abrir_mapa(self):
        for localizacao in LOCALIZACOES:
            if localizacao in self.caminho:
                folium.Marker((localizacao.obter_latitude(), localizacao.obter_longitude())).add_to(self.mapa)

        coordenadas = []
        for c in self.caminho:
            coordenadas.append((c.latitude, c.longitude))
        polyline = folium.PolyLine(coordenadas, color="blue").add_to(self.mapa)

        """texto_rotulo = "Seu rótulo aqui"
        offset = 0.004
        tamanho_fonte = 30
        folium.plugins.PolyLineTextPath(polyline, texto_rotulo, offset=offset, text_font=tamanho_fonte).add_to(self.mapa)"""

        self.mapa.save(TEMP_MAP_PATH)
        webbrowser.open(TEMP_MAP_PATH)
