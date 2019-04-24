from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_node(self, node_to_add):
        if node_to_add not in self.graph:
            self.graph[node_to_add] = {}

    def remove_node(self, node_to_remove):
        if node_to_remove in self.graph:
            for connected_edges in self.graph.values():
                if node_to_remove in connected_edges:
                    connected_edges.remove(node_to_remove)
            del self.graph[node_to_remove]

    def add_edge(self, from_node, to_node):
        if from_node in self.graph and to_node in self.graph:
            self.graph[from_node].add(to_node)
            self.graph[to_node].add(from_node)

    def remove_edge(self, from_node, to_node):
        if from_node in self.graph and to_node in self.graph:
            if to_node in self.graph[from_node]:
                self.graph[from_node].remove(to_node)

            if from_node in self.graph[to_node]:
                self.graph[to_node].remove(from_node)
