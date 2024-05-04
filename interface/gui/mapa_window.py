import webbrowser

import folium

from constants import TEMP_MAP_PATH
from data import LOCALIZACOES, PAISES, CONEXOES
from folium import plugins


class Mapa:
    def __init__(self, caminho):
        self.caminho = caminho
        self.mapa = folium.Map(location=[self.caminho[0].obter_latitude(), self.caminho[0].obter_longitude()],
                               zoom_start=10)

    def abrir_mapa(self):
        self.__create_makers()
        self.__create_polylines()

        self.mapa.save(TEMP_MAP_PATH)
        webbrowser.open(TEMP_MAP_PATH)

    def __create_polylines(self):
        for i in range(len(self.caminho) - 1):
            origem = self.caminho[i]
            destino = self.caminho[i + 1]
            coordenadas = [(origem.latitude, origem.longitude),
                           (destino.latitude, destino.longitude)]
            polyline = folium.PolyLine(coordenadas, color="blue").add_to(self.mapa)
            distancia_reta = PAISES.calcular_distancia_reta(origem, destino)
            distancia = CONEXOES.get_distance(origem, destino)
            texto_distancia_reta = str(distancia_reta) + " km/reto"
            texto_distancia = str(distancia) + " km"
            offset = 1
            style = ("font-family: Arial; font-weight: bold; font-size: 18px; fill: black; "
                     "text-shadow: 0px 0px 7px rgba(0,0,0);")
            attributes = {'style': style}
            folium.plugins.PolyLineTextPath(
                polyline,
                texto_distancia_reta + " | " + texto_distancia,
                offset=offset,
                attributes=attributes,
            ).add_to(self.mapa)

    def __create_makers(self):
        first_l = self.caminho[0]
        last_l = self.caminho[-1]
        cor_origem = 'red'
        cor_chegada = 'green'
        for localizacao in LOCALIZACOES:
            if localizacao in self.caminho:
                icon = None
                popup = self.__marker_popup(localizacao)
                if localizacao == first_l:
                    icon = folium.Icon(color=cor_origem, icon='star')
                    popup = "Origem | " + popup
                elif localizacao == last_l:
                    icon = folium.Icon(color=cor_chegada, icon='info-sign')
                    popup = "Destino | " + popup

                folium.Marker(
                    location=(localizacao.obter_latitude(), localizacao.obter_longitude()),
                    popup=popup,
                    icon=icon
                ).add_to(self.mapa)

    @staticmethod
    def __marker_popup(localizacao):
        marker_popup_text = ""
        marker_popup_text += localizacao.obter_nome() + "\n"
        marker_popup_text += str(localizacao.obter_latitude()) + " " + str(localizacao.obter_longitude())
        return marker_popup_text
