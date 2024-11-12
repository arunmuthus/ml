from collections import defaultdict

# Bellman-Ford based Distance Vector Routing
def distance_vector(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    predecessor = {node: None for node in graph}

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, cost in graph[u].items():
                if distance[u] + cost < distance[v]:
                    distance[v] = distance[u] + cost
                    predecessor[v] = u

    return distance, predecessor

# Example graph representation as adjacency list
graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'B': 1, 'D': 1},
    'D': {'A': 3, 'C': 1}
}

source = 'A'
distance, predecessor = distance_vector(graph, source)
print("Distance from source:", distance)
print("Predecessors:", predecessor)
