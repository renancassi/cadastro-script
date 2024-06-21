import random
from shapely.geometry import Point, Polygon
from geopy.distance import distance

def generate_random_point_in_polygon(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        if polygon.contains(random_point):
            return random_point

def generate_random_point_around(center_point, radius_meters):
    angle = random.uniform(0, 360)
    distance_meters = random.uniform(0, radius_meters)
    return distance(meters=distance_meters).destination((center_point.y, center_point.x), angle)

city_polygons = {
    'Dois Vizinhos': Polygon([
        (-53.0928, -25.7761),
        (-53.0928, -25.7226),
        (-53.0329, -25.7226),
        (-53.0329, -25.7761)
    ])
}

cto_coords = [
    (-53.05674983032025, -25.734461804972586),
    (-53.05627962499026, -25.732525908667245),
    (-53.05142168114123, -25.741015500358817),
    (-53.0660772711986, -25.758255136837647),
    (-53.07040195226136, -25.73021051552297),
    (-53.071131513113414, -25.73736243965864),
    (-53.06748370885316, -25.74391477076708),
    (-53.07153920888368, -25.755124410824227),
    (-53.078083798880016, -25.75701834898086),
    (-53.05741308103556, -25.755606604518643),
    (-53.05382222429283, -25.74715746439674),
    (-53.056631814404355, -25.74220998640037),
    (-53.05041996979124, -25.756396861200546),
    (-53.06174960524505, -25.746446006488043),
    (-53.050616552781825, -25.74844718781723),
    (-53.07692981888188, -25.74669741590945),
    (-53.05630274683756, -25.76687760910119)
]

def get_random_coordinates_around_ctos(cto_coords, radius_meters=800):
    random_coords = []
    for cto in cto_coords:
        cto_point = Point(cto[1], cto[0])
        random_point = generate_random_point_around(cto_point, radius_meters)
        random_coords.append((random_point.latitude, random_point.longitude))
    return random_coords

random_cto_coords = get_random_coordinates_around_ctos(cto_coords)
for coord in random_cto_coords:
    print(f"Lat: {coord[0]}, Lon: {coord[1]}")
