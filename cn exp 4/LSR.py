import heapq

# Dijkstra's algorithm for Link State Routing
def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, predecessors

# Example graph representation as adjacency list
graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'B': 1, 'D': 1},
    'D': {'A': 3, 'C': 1}
}

start = 'A'
distances, predecessors = dijkstra(graph, start)
print("Distances from start:", distances)
print("Predecessors:", predecessors)
