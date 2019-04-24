from src.datastructures.graph import Graph

def test_add_node_to_empty_graph():
    graph = Graph()
    graph.add_node("Test")

    expected = {"Test": {}}
    output = graph.graph
    assert output == expected

def test_add_same_node_twice():
    graph = Graph()
    graph.add_node("Node_1")
    graph.add_node("Node_1")

    expected = {"Node_1": {}}
    output = graph.graph
    assert output == expected

def test_add_node_different_types_multiple():
    graph = Graph()
    graph.add_node("Node_1")
    graph.add_node(1)
    graph.add_node(2.3456)

    expected = {"Node_1": {}, 1: {}, 2.3456: {}}
    output = graph.graph
    assert output == expected

def test_remove_node_does_not_exist():
    graph = Graph()
    graph.graph["test_node"] = {}
    graph.remove_node("test")
    
    expected = {"test_node": {}}
    output = graph.graph
    assert output == expected

def test_remove_node_with_no_edges():
    graph = Graph()
    graph.graph["node_1"] = {}
    graph.graph["node_2"] = {}
    graph.graph["node_3"] = {}
    graph.remove_node("node_1")

    expected = {"node_2": {}, "node_3": {}}
    output = graph.graph
    assert output == expected

def test_remove_node_with_edges():
    graph = Graph()
    graph.graph[1] = {2, 3}
    graph.graph[2] = {4}
    graph.graph[3] = {3}
    graph.graph[4] = {1, 2}
    graph.remove_node(3)

    expected = {1: {2}, 2: {4}, 4: {1, 2}}
    output = graph.graph
    assert output == expected

def test_add_edge_node_does_node_exist():
    graph = Graph()
    graph.add_edge(1, 2)

    expected = {}
    output = graph.graph
    assert output == expected

def test_add_edge_node_to_itself():
    graph = Graph()
    graph.graph["node_1"] = set()
    graph.add_edge("node_1", "node_1")

    expected = {"node_1": {"node_1"}}
    output = graph.graph
    assert output == expected

def test_add_edge_node_to_multiple_nodes():
    graph = Graph()
    graph.graph[1] = set()
    graph.graph[2] = set()
    graph.graph[3] = set()
    graph.add_edge(1, 2)
    graph.add_edge(2, 2)
    graph.add_edge(3, 2)
    graph.add_edge(1, 3)

    expected = {1: {2, 3}, 2: {1, 2, 3}, 3: {2, 1}}
    output = graph.graph
    assert output == expected

def test_remove_edge_from_empty_graph():
    graph = Graph()
    graph.remove_edge("A", "B")

    expected = {}
    output = graph.graph
    assert output == expected

def test_remove_edge_one_not_in_graph():
    graph = Graph()
    graph.graph['A'] = set([1, 2, 3])
    graph.remove_edge('A', 6)

    expected = {'A': {1, 2, 3}}
    output = graph.graph
    assert output == expected

def test_remove_edge_normal_case():
    graph = Graph()
    graph.graph[1] = set()
    graph.graph[2] = set()
    graph.graph[1].add(2)
    graph.graph[1].add(3)
    graph.graph[2].add(1)
    graph.graph[2].add(3)
    graph.remove_edge(2, 1)

    expected = {1: {3}, 2: {3}}
    output = graph.graph
    assert output == expected

def test_remove_one_directed_edge():
    graph = Graph()
    graph.graph[1] = set()
    graph.graph[2] = set()
    graph.graph[1].add(2)
    graph.graph[1].add(3)
    graph.graph[2].add(3)
    graph.remove_edge(1, 2)

    expected = {1: {3}, 2: {3}}
    output = graph.graph
    assert output == expected
