import random
from shapely.geometry import Point, Polygon

def generate_random_point_in_polygon(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        if polygon.contains(random_point):
            return random_point

# Definição dos limites das cidades
city_polygons = {
    'Dois Vizinhos': Polygon([
        (-53.0928, -25.7761),  # Sul, Oeste
        (-53.0928, -25.7226),  # Norte, Oeste
        (-53.0329, -25.7226),  # Norte, Leste
        (-53.0329, -25.7761)   # Sul, Leste
    ]),
  
  'Francisco Beltrão': Polygon([
    (-53.0763, -26.0930),  # Sul, Oeste
    (-53.0763, -26.0284),  # Norte, Oeste
    (-53.0324, -26.0284),  # Norte, Leste
    (-53.0324, -26.0930)   # Sul, Leste
    ]),

  'Pato Branco': Polygon([
    (-52.7174, -26.2696),  # Sul, Oeste
    (-52.7174, -26.1906),  # Norte, Oeste
    (-52.6492, -26.1906),  # Norte, Leste
    (-52.6492, -26.2696)   # Sul, Leste
    ])

}

def get_random_coordinates(city_name):
    if city_name in city_polygons:
        polygon = city_polygons[city_name]
        point = generate_random_point_in_polygon(polygon)
        return point.y, point.x 
        
    else:
        raise ValueError(f"Coordenadas não definidas para a cidade: {city_name}")

doisvizinhos = 'Dois Vizinhos'
beltrao = 'Francisco Beltrão'
patobranco = 'Pato Branco'

coordenadaDvY, coordenadaDvX = get_random_coordinates(doisvizinhos)
coordenadaFbY, coordenadaFbX = get_random_coordinates(beltrao)
coordenadaPbY, coordenadaPbX = get_random_coordinates(patobranco)

#Testar coordenadas
#print(f'Dois Vizinhos: https://www.google.com/maps/search/{coordenadaDvY},+{coordenadaDvX}?sa=X&ved=1t:242&ictx=111\n')
#print(f'Beltrão: https://www.google.com/maps/search/{coordenadaFbY},+{coordenadaFbX}?sa=X&ved=1t:242&ictx=111\n')
#print(f'Pato Branco: https://www.google.com/maps/search/{coordenadaPbY},+{coordenadaPbX}?sa=X&ved=1t:242&ictx=111')
