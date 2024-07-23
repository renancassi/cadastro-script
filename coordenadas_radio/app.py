from shapely.geometry import Point
from geopy.distance import distance
import pandas as pd
import random

clientes_pontos_radio = 'C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/loc_ponto_radio.csv'

def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    return distance(meters=distance_meters).destination((center_point.y, center_point.x), angle)


def get_coordinates_from_csv(file_path):
    cto_data = pd.read_csv(file_path, sep=';')
    cto_coords = []

    for index, row in cto_data.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        city_name = row['Cidade']
        cto_coords.append((lon, lat, city_name))

    return cto_coords

def atualizarCoordenadasPonto(client_data, cto_coords, radius_meters=500):
    updated_clients = []
    for client in client_data:
        client_lat, client_lon, client_neighborhood, client_city = client
        updated = False
        for cto in cto_coords:
            if cto[2] == client_neighborhood and cto[3] == client_city:
                cto_point = Point(cto[1], cto[0])
                random_point = generate_random_point_around(cto_point, radius_meters)
                updated_clients.append((random_point.latitude, random_point.longitude, client_neighborhood, client_city))
                updated = True
                break
        if not updated:
            updated_clients.append((client_lat, client_lon, client_neighborhood, client_city))
    return updated_clients
