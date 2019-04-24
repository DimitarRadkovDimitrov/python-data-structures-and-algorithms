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
