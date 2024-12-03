import math

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_airport(self, airport):
        self.nodes[airport.code] = airport
        self.edges[airport.code] = []

    def add_connection(self, from_code, to_code):
        if from_code in self.nodes and to_code in self.nodes:
            distance = self.calculate_distance(self.nodes[from_code], self.nodes[to_code])
            self.edges[from_code].append((to_code, distance))
            self.edges[to_code].append((from_code, distance))

    def calculate_distance(self, airport1, airport2):
        return haversine(airport1.longitude, airport1.latitude, airport2.longitude, airport2.latitude)

def haversine(lon1, lat1, lon2, lat2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
