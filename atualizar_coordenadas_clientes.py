import random
import pandas as pd
from shapely.geometry import Point
from geopy.distance import distance
import xml.etree.ElementTree as ET

def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    return distance(meters=distance_meters).destination((center_point.y, center_point.x), angle)

def get_coordinates_from_kml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {"kml": "http://www.opengis.net/kml/2.2"}
    cto_coords = []
    city_name = root.find(".//kml:Document/kml:name", namespace).text.strip()

    for placemark in root.findall(".//kml:Placemark", namespace):
        point = placemark.find("kml:Point", namespace)
        if point is not None:
            coordinates = point.find("kml:coordinates", namespace).text.strip()
            lon, lat = map(float, coordinates.split(","))
            
            description = placemark.find("kml:description", namespace).text.strip() if placemark.find("kml:description", namespace) is not None else None
            
            style_url = placemark.find("kml:styleUrl", namespace).text.strip() if placemark.find("kml:styleUrl", namespace) is not None else None
            if style_url and "#stl-cto" in style_url:
                cto_coords.append((lon, lat, description, city_name))
    
    return cto_coords

def get_random_coordinates_around_ctos(cto_coords, radius_meters=500):
    random_coords = []
    for cto in cto_coords:
        cto_point = Point(cto[1], cto[0])
        random_point = generate_random_point_around(cto_point, radius_meters)
        random_coords.append((random_point.latitude, random_point.longitude, cto[2], cto[3]))  # Include description and city
    return random_coords

def update_client_coordinates(client_data, cto_coords, radius_meters=500):
    updated_clients = []
    for client in client_data:
        client_lat, client_lon, client_neighborhood, client_city = client
        for cto in cto_coords:
            if cto[2] == client_neighborhood and cto[3] == client_city:
                cto_point = Point(cto[1], cto[0])
                random_point = generate_random_point_around(cto_point, radius_meters)
                updated_clients.append((random_point.latitude, random_point.longitude, client_neighborhood, client_city))
                break
        else:
            updated_clients.append((client_lat, client_lon, client_neighborhood, client_city))
    return updated_clients

# Carregar os dados do CSV
csv_file = 'clientes/clientes_import.csv'
client_data = pd.read_csv(csv_file)

# Processar os arquivos KML e obter coordenadas CTO
kml_files = ['cidadesOlt/doisVizinhos.kml', 'cidadesOlt/franciscoBeltrao.kml', 'cidadesOlt/patoBranco.kml']
all_cto_coords = []
for kml_file in kml_files:
    cto_coords = get_coordinates_from_kml(kml_file)
    all_cto_coords.extend(cto_coords)

# Atualizar as coordenadas dos clientes
client_coordinates = client_data[['ponto_end_latitude', 'ponto_end_longitude', 'ponto_end_bairro', 'ponto_end_cidade']].values.tolist()
updated_client_coords = update_client_coordinates(client_coordinates, all_cto_coords, radius_meters=500)

# Atualizar o DataFrame original com as novas coordenadas
for i, updated_coord in enumerate(updated_client_coords):
    client_data.at[i, 'ponto_end_longitude'] = updated_coord[1]
    client_data.at[i, 'ponto_end_latitude'] = updated_coord[0]
    client_data.at[i, 'ponto_end_bairro'] = updated_coord[2]
    client_data.at[i, 'ponto_end_cidade'] = updated_coord[3]

# Salvar o DataFrame atualizado em um novo arquivo CSV
client_data.to_excel('clientes/clientes_atualizados.xlsx', index=False)
