from src.graph import Graph

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

def test_depth_first_search_one_node_graph(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.depth_first_search('A')

    expected = "A "
    output = capsys.readouterr().out
    assert output == expected

def test_depth_first_search_with_cycles(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.graph['B'] = set()
    graph.graph['C'] = set()
    graph.graph['D'] = set()
    graph.graph['E'] = set()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.depth_first_search('A')

    expected = "A B C D E "
    output = capsys.readouterr().out
    assert output == expected

def test_depth_first_search_complex(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.graph['B'] = set()
    graph.graph['C'] = set()
    graph.graph['D'] = set()
    graph.graph['E'] = set()
    graph.graph['F'] = set()
    graph.graph['G'] = set()
    graph.graph['H'] = set()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'G')
    graph.add_edge('E', 'H')
    graph.add_edge('F', 'H')
    graph.add_edge('G', 'H')
    graph.depth_first_search('A')

    expected = "A B E H F C G D "
    output = capsys.readouterr().out
    assert output == expected

def test_breadth_first_search_one_node_graph(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.breadth_first_search('A')

    expected = "A "
    output = capsys.readouterr().out
    assert output == expected

def test_breadth_first_search_with_cycles(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.graph['B'] = set()
    graph.graph['C'] = set()
    graph.graph['D'] = set()
    graph.graph['E'] = set()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.breadth_first_search('A')

    expected = "A B C D E "
    output = capsys.readouterr().out
    assert output == expected

def test_breadth_first_search_complex(capsys):
    graph = Graph()
    graph.graph['A'] = set()
    graph.graph['B'] = set()
    graph.graph['C'] = set()
    graph.graph['D'] = set()
    graph.graph['E'] = set()
    graph.graph['F'] = set()
    graph.graph['G'] = set()
    graph.graph['H'] = set()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'G')
    graph.add_edge('E', 'H')
    graph.add_edge('F', 'H')
    graph.add_edge('G', 'H')
    graph.breadth_first_search('A')

    expected = "A B C D E F G H "
    output = capsys.readouterr().out
    assert output == expected
