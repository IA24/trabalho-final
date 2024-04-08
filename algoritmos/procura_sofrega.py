'''def busca_sofrega(origem, destino, distancias, distancias_faro):
    caminho = [origem]
    while caminho[-1] != destino:
        cidade_atual = caminho[-1]
        proxima_cidade = None
        menor_distancia = float('inf')
        for adjacente in distancias[cidade_atual]:
            if adjacente not in caminho:
                distancia = distancias_faro[adjacente]
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    proxima_cidade = adjacente
        if proxima_cidade is None:
            print("Não foi possível encontrar um caminho até o destino.")
            return None
        caminho.append(proxima_cidade)
    return caminho

# Exemplo de utilização
caminho = busca_sofrega('Aveiro', 'Faro', distancias, distancias_faro)
if caminho:
    print("Caminho encontrado:", caminho)
'''