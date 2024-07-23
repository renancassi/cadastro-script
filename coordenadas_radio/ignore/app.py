import random
import pandas as pd
from shapely.geometry import Point
from geopy.distance import geodesic

def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    destination = geodesic(meters=distance_meters).destination((center_point.y, center_point.x), angle)
    return Point(destination.longitude, destination.latitude)

def update_client_coordinates(client_data, cto_data, radius_meters=20):
    bairros_cto = cto_data['Bairro'].unique().tolist()
    updated_clients = []
    
    for index, client in client_data.iterrows():
        client_bairro = client['Bairro']
        
        if client_bairro not in bairros_cto:
            random_cto = cto_data.sample(n=1).iloc[0]
            client['Bairro'] = random_cto['Bairro']
            cto_point = Point(random_cto['mapa_lon'], random_cto['mapa_lat'])
            random_point = generate_random_point_around(cto_point, radius_meters)
            client['Latitude'] = random_point.y
            client['Longitude'] = random_point.x
            
        updated_clients.append(client)
        
    return pd.DataFrame(updated_clients)

# Leitura dos arquivos CSV
pontos_radio_beltrao_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/cto.csv')
cto_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/cto.csv')

# Atualização dos dados dos clientes
updated_clients_df = update_client_coordinates(pontos_radio_beltrao_df, cto_df, radius_meters=20)

# Salvando o resultado atualizado em um novo arquivo
updated_clients_df.to_csv('././coordenadas_radio/pontos_radio_beltrao_atualizado.csv', index=False)
