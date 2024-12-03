from collections import deque
import heapq
from typing import List, Set, Tuple
from graph import Graph

class GraphAlgorithms:
    def __init__(self, graph: Graph):
        self.graph = graph

    def bfs(self, start: str, end: str) -> Tuple[List[str], float]:

        if start not in self.graph.nodes or end not in self.graph.nodes:
            return [], 0

        queue = deque([(start, [start], 0)])
        visited = {start}

        while queue:
            current, path, distance = queue.popleft()
            
            if current == end:
                return path, distance

            for neighbor, edge_distance in self.graph.edges[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path, distance + edge_distance))

        return [], 0

    def dfs(self, start: str, end: str) -> Tuple[List[str], float]:
        
        def dfs_recursive(current: str, visited: Set[str], path: List[str], distance: float) -> Tuple[List[str], float]:
            if current == end:
                return path, distance

            visited.add(current)
            for neighbor, edge_distance in self.graph.edges[current]:
                if neighbor not in visited:
                    result_path, result_distance = dfs_recursive(neighbor, visited, path + [neighbor], distance + edge_distance)
                    if result_path:
                        return result_path, result_distance
            
            return [], 0

        if start not in self.graph.nodes or end not in self.graph.nodes:
            return [], 0

        return dfs_recursive(start, set(), [start], 0)

    def dijkstra(self, start: str, end: str) -> Tuple[List[str], float]:
        
        if start not in self.graph.nodes or end not in self.graph.nodes:
            return [], 0

        distances = {airport: float('infinity') for airport in self.graph.nodes}
        distances[start] = 0
        previous = {airport: None for airport in self.graph.nodes}
        pq = [(0, start)]
        visited = set()

        while pq:
            current_distance, current = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)

            if current == end:
                break

            for neighbor, edge_distance in self.graph.edges[current]:
                if neighbor in visited:
                    continue
                    
                distance = current_distance + edge_distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))

        if distances[end] == float('infinity'):
            return [], 0

        # Reconstruct path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path, distances[end] 
