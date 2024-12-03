from airport import Airport
from graph import Graph

def initialize_graph():
    airports = [
        Airport("ATL", "Atlanta", "GA", 84.3880, 33.7490),
        Airport("AUS", "Austin", "TX", 97.7431, 30.2672),
        # ... add all other airports ...
    ]

    neighbours = [
        ["RDU", "AUS", "BOS", "BWI", "DCA", "DEN", "DFW", "DTW", "EWR", "IAD",
         "IAH", "JFK", "LAS", "LAX", "MDW", "MIA", "MSP", "PDX", "PHL", "SAN",
         "SEA", "SFO", "SLC"],
        # ... add all other connections ...
    ]

    graph = Graph()
    for airport in airports:
        graph.add_airport(airport)

    for i, airport in enumerate(airports):
        for neighbour in neighbours[i]:
            graph.add_connection(airport.code, neighbour)

    return graph 
