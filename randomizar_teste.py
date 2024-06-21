import random
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
    
    for placemark in root.findall(".//kml:Placemark", namespace):
        point = placemark.find("kml:Point", namespace)
        if point is not None:
            coordinates = point.find("kml:coordinates", namespace).text.strip()
            lon, lat = map(float, coordinates.split(","))
            
  
            description = placemark.find("kml:description", namespace).text.strip() if placemark.find("kml:description", namespace) is not None else None
            

            style_url = placemark.find("kml:styleUrl", namespace).text.strip() if placemark.find("kml:styleUrl", namespace) is not None else None
            if style_url and "#stl-cto" in style_url:
                cto_coords.append((lon, lat, description))
    
    return cto_coords

def get_random_coordinates_around_ctos(cto_coords, radius_meters=500):
    random_coords = []
    for cto in cto_coords:
        cto_point = Point(cto[1], cto[0])
        random_point = generate_random_point_around(cto_point, radius_meters)
        random_coords.append((random_point.latitude, random_point.longitude, cto[2]))  # Include description
    return random_coords

def process_kml_file(kml_file):
    cto_coords = get_coordinates_from_kml(kml_file)
    random_cto_coords = get_random_coordinates_around_ctos(cto_coords, radius_meters=500)  # Adjusted radius to 500 meters
    
    print(f"=== Coordenadas Aleatórias para o arquivo: {kml_file} ===")
    for coord in random_cto_coords:
        print(f"Lat: {coord[0]}, Lon: {coord[1]}, Neighborhood: {coord[2]}")
    print("\n")

# Lista com os caminhos dos arquivos KML das outras cidades
kml_files = ['cidadesOlt/doisVizinhos.kml', 'cidadesOlt/franciscoBeltrao.kml']

# Processar cada arquivo KML
for kml_file in kml_files:
    process_kml_file(kml_file)
