import random
import pandas as pd
from shapely.geometry import Point
from geopy.distance import distance

# Função para gerar um ponto aleatório ao redor de um ponto central dentro de um raio
def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    return distance(meters=distance_meters).destination((center_point.y, center_point.x), angle)

# Função para atualizar as coordenadas dos clientes
def update_client_coordinates(client_data, cto_coords, radius_meters=300):
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

# Carregar os arquivos CSV
clientes_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/pronto/cliente_cep.csv')
coordenadas_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/pronto/coordenadas_bairros.csv')

# Preparar os dados para processamento
clientes_data = clientes_df[['latitude', 'longitude', 'bairro', 'Cidade']].values.tolist()
coordenadas_data = coordenadas_df[['latitude', 'longitude', 'bairro', 'Cidade']].values.tolist()

# Atualizar as coordenadas dos clientes
updated_clients = update_client_coordinates(clientes_data, coordenadas_data)

# Atualizar o dataframe com as novas coordenadas
clientes_df['latitude'] = [client[0] for client in updated_clients]
clientes_df['longitude'] = [client[1] for client in updated_clients]

# Salvar o resultado em um novo arquivo CSV
clientes_df.to_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/pronto/cliente_atualizado_pronto.csv', index=False)

print("Coordenadas atualizadas e salvas em 'clientes_com_coordenadas.csv'.")
