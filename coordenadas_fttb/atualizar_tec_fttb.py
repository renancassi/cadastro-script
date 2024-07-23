import random
import pandas as pd
from shapely.geometry import Point
from geopy.distance import distance

def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    return distance(meters=distance_meters).destination((center_point.y, center_point.x), angle)

def get_coordinates_from_csv(file_path):
    cto_data = pd.read_csv(file_path)
    cto_coords = []

    for index, row in cto_data.iterrows():
        lat = row['mapa_lat']
        lon = row['mapa_lon']
        description = row['descricao']
        city_name = row['nome']
        cto_coords.append((lon, lat, description, city_name))
    
    return cto_coords

def update_client_coordinates(client_data, cto_coords, radius_meters=3):
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


csv_file_clients = './clientes_doisVizinhos.csv.csv'
client_data = pd.read_csv(csv_file_clients)


csv_file_ctos = 'cidadesOlt/cto_cidades.csv'
cto_coords = get_coordinates_from_csv(csv_file_ctos)


client_coordinates = client_data[['ponto_end_latitude', 'ponto_end_longitude', 'ponto_end_bairro', 'ponto_end_cidade']].values.tolist()
updated_client_coords = update_client_coordinates(client_coordinates, cto_coords, radius_meters=500)


for i, updated_coord in enumerate(updated_client_coords):
    client_data.at[i, 'ponto_end_latitude'] = updated_coord[1]
    client_data.at[i, 'ponto_end_longitude'] = updated_coord[0]
    client_data.at[i, 'ponto_end_bairro'] = updated_coord[2]
    client_data.at[i, 'ponto_end_cidade'] = updated_coord[3]


client_data.to_csv('clientes/clientes_coordenadas_fttb.csv', index=False)
