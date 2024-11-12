import heapq
class LinkStateRouting:
    def __init__(self, graph):
        self.graph = graph
    def dijkstra(self, source):
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        priority_queue = [(0, source)]
        predecessors = {node: None for node in self.graph}
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances, predecessors
    def get_shortest_path(self, predecessors, target):
        path = []
        while target is not None:
            path.insert(0, target)
            target = predecessors[target]
        return path
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    ls_router = LinkStateRouting(graph)
    distances, predecessors = ls_router.dijkstra('A')
    target = 'D'
    print(f"Shortest path from A to {target}: {ls_router.get_shortest_path(predecessors, target)}")
    print(f"Distances from A: {distances}")