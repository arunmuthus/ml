class DistanceVectorRouting:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {}
        self.predecessors = {}
    def initialize(self, source):
        self.distances = {node: float('inf') for node in self.graph}
        self.predecessors = {node: None for node in self.graph}
        self.distances[source] = 0
    def relax_edges(self):
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                if self.distances[node] + weight < self.distances[neighbor]:
                    self.distances[neighbor] = self.distances[node] + weight
                    self.predecessors[neighbor] = node
    def compute_routing_table(self, source):
        self.initialize(source)
        for _ in range(len(self.graph) - 1):
            self.relax_edges()
    def get_shortest_path(self, target):
        path = []
        while target is not None:
            path.insert(0, target)
            target = self.predecessors[target]
        return path
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 1, 'D': 5},
        'C': {'A': 4, 'B': 5, 'D': 1},
        'D': {'B': 5, 'C': 4}
    }
    
    dv_router = DistanceVectorRouting(graph)
    dv_router.compute_routing_table('A')
    target = 'C'
    print(f"Shortest path from A to {target}: {dv_router.get_shortest_path(target)}")
    print(f"Distances from A: {dv_router.distances}")