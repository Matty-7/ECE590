from airport import Airport
from graph import Graph

def initialize_graph():
    airports = [
        Airport("ATL", "Atlanta", "GA", 84.3880, 33.7490),
        Airport("AUS", "Austin", "TX", 97.7431, 30.2672),
        Airport("BOS", "Boston", "MA", 71.0096, 42.3656),
        Airport("BWI", "Baltimore", "MD", 76.6413, 39.2904),
        Airport("DCA", "Washington D.C.", "VA", 77.0369, 38.9072),
        Airport("DEN", "Denver", "CO", 104.9903, 39.7392),
        Airport("DFW", "Dallas", "TX", 96.7967, 32.7767),
        Airport("DTW", "Detroit", "MI", 83.0458, 42.3314),
        Airport("EWR", "Newark", "NJ", 74.1745, 40.7357),
        Airport("IAD", "Washington D.C.", "VA", 77.4558, 38.8821),
        Airport("IAH", "Houston", "TX", 95.3698, 29.7604),
        Airport("JFK", "New York City", "NY", 73.7781, 40.6413),
        Airport("LAS", "Las Vegas", "NV", 115.1398, 36.1699),
        Airport("LAX", "Los Angeles", "CA", 118.2437, 34.0522),
        Airport("MDW", "Chicago", "IL", 87.6298, 41.8781),
        Airport("MIA", "Miami", "FL", 80.1918, 25.7617),
        Airport("MSP", "Minneapolis and Saint Paul", "MN", 93.2650, 44.9778),
        Airport("PDX", "Portland", "OR", 122.6762, 45.5051),
        Airport("PHL", "Philadelphia", "PA", 75.1652, 39.9526),
        Airport("PHX", "Phoenix", "AZ", 112.008629, 33.437309),
        Airport("RDU", "Raleigh and Durham", "NC", 78.7870, 35.7796),
        Airport("SAN", "San Diego", "CA", 117.1611, 32.7157),
        Airport("SEA", "Seattle", "WA", 122.3321, 47.6062),
        Airport("SFO", "San Francisco", "CA", 122.4194, 37.7749),
        Airport("SLC", "Salt Lake City", "UT", 111.8910, 40.7608)
    ]

    neighbours = [
        ["RDU", "AUS", "BOS", "BWI", "DCA", "DEN", "DFW", "DTW", "EWR", "IAD", "IAH", "JFK", "LAS", "LAX", "MDW", "MIA", "MSP", "PDX", "PHL", "SAN", "SEA", "SFO", "SLC"],
        ["ATL", "BOS", "DTW", "JFK", "RDU", "LAS", "LAX", "MSP", "SEA", "SLC"],
        ["SLC", "RDU", "AUS", "ATL", "DTW", "MSP", "SEA", "LAX", "DEN", "JFK", "IAD", "MIA", "PHL", "IAH", "LAS"],
        ["ATL", "DTW", "MSP", "JFK", "SLC", "BOS"],
        ["ATL", "JFK", "BOS", "DTW", "MSP", "SLC"],
        ["ATL", "MSP", "SLC", "DTW"],
        ["ATL", "MSP", "DTW", "SLC"],
        ["ATL", "MSP", "DTW", "SLC", "LAX"],
        ["BOS", "JFK", "ATL", "RDU", "MIA", "LAX", "SFO", "SEA"],
        ["ATL", "BOS", "DTW", "MSP", "RDU", "SLC"],
        ["ATL", "DTW", "SLC"],
        ["ATL", "DTW", "MSP", "SLC"],
        ["LAX", "ATL", "MIA", "DFW", "BOS", "SFO", "DTW", "SEA", "MSP"],
        ["ATL", "MSP", "DTW", "SLC", "LAX", "SEA", "SFO", "DFW"],
        ["JFK", "SFO", "SLC", "ATL", "LAS", "MSP", "BOS", "DTW", "SEA", "PDX"],
        ["ATL", "DTW", "MSP"],
        ["ATL", "JFK", "LAX", "BOS", "DFW", "DCA"],
        ["ATL", "DEN", "DFW", "SEA", "LAS", "LAX"],
        ["SEA", "LAX", "SFO", "SLC", "MSP", "ATL", "DTW"],
        ["ATL", "BOS", "JFK", "DTW", "MSP", "SLC"],
        ["ATL", "BOS", "DTW", "MSP", "LAX", "SLC"],
        ["MSP", "SEA", "SLC", "ATL", "DTW", "JFK"],
        ["LAX", "SLC", "ATL", "MSP", "SFO", "DFW", "DEN", "LAS"],
        ["LAX", "JFK", "SAN", "SEA", "DEN", "SLC", "DFW", "PDX"],
        ["LAX", "DEN", "PHX", "SEA", "ATL", "MSP", "LAS"]
    ]

    graph = Graph()
    for airport in airports:
        graph.add_airport(airport)

    for i, airport in enumerate(airports):
        for neighbour in neighbours[i]:
            graph.add_connection(airport.code, neighbour)

    return graph 
