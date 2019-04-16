from src.binary_tree_node import Binary_Tree_Node

def test_in_order_print_one_node(capsys):
    root_node = Binary_Tree_Node(1)
    root_node.in_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_in_order_print_multiple_nodes(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.left_child = Binary_Tree_Node(1)
    root_node.left_child.left_child = Binary_Tree_Node(7)
    root_node.left_child.right_child = Binary_Tree_Node(9)
    root_node.right_child = Binary_Tree_Node(5)
    root_node.right_child.left_child = Binary_Tree_Node(2)
    root_node.right_child.right_child = Binary_Tree_Node(6)
    root_node.in_order_print(root_node)

    expected = "7 1 9 4 2 5 6 "
    output = capsys.readouterr().out
    assert output == expected

def test_pre_order_print_one_node(capsys):
    root_node = Binary_Tree_Node(1)
    root_node.pre_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_pre_order_print_multiple_nodes(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.left_child = Binary_Tree_Node(1)
    root_node.left_child.left_child = Binary_Tree_Node(7)
    root_node.left_child.right_child = Binary_Tree_Node(9)
    root_node.right_child = Binary_Tree_Node(5)
    root_node.right_child.left_child = Binary_Tree_Node(2)
    root_node.right_child.right_child = Binary_Tree_Node(6)
    root_node.pre_order_print(root_node)

    expected = "4 1 7 9 5 2 6 "
    output = capsys.readouterr().out
    assert output == expected

def test_post_order_print_one_node(capsys):
    root_node = Binary_Tree_Node(1)
    root_node.post_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_post_order_print_multiple_nodes(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.left_child = Binary_Tree_Node(1)
    root_node.left_child.left_child = Binary_Tree_Node(7)
    root_node.left_child.right_child = Binary_Tree_Node(9)
    root_node.right_child = Binary_Tree_Node(5)
    root_node.right_child.left_child = Binary_Tree_Node(2)
    root_node.right_child.right_child = Binary_Tree_Node(6)
    root_node.post_order_print(root_node)

    expected = "7 9 1 2 6 5 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_one_node(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.insert(2)
    root_node.in_order_print(root_node)
    
    expected = "2 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_same_node_twice(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.insert(2)
    root_node.insert(2)
    root_node.in_order_print(root_node)

    expected = "2 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_multiple_nodes(capsys):
    root_node = Binary_Tree_Node(4)
    root_node.insert(2)
    root_node.insert(1)
    root_node.insert(7)
    root_node.insert(5)
    root_node.insert(6)
    root_node.insert(3)
    root_node.in_order_print(root_node)

    expected = "1 2 3 4 5 6 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_as_multiple_nodes_as_linked_list(capsys):
    root_node = Binary_Tree_Node(1)
    root_node.insert(3)
    root_node.insert(5)
    root_node.insert(7)
    root_node.in_order_print(root_node)

    expected = "1 3 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_find_node_in_one_node_tree():
    root_node = Binary_Tree_Node(7)
    
    expected = True
    output = root_node.find(7)
    assert output == expected

def test_find_node_not_in_one_node_tree():
    root_node = Binary_Tree_Node(7)
    
    expected = False
    output = root_node.find(1)
    assert output == expected

def test_find_node_in_full_tree():
    root_node = Binary_Tree_Node(4)
    root_node.insert(2)
    root_node.insert(1)
    root_node.insert(7)
    root_node.insert(5)
    root_node.insert(6)
    root_node.insert(3)

    expected = True
    output = root_node.find(3)
    assert output == expected

def test_find_node_not_in_full_tree():
    root_node = Binary_Tree_Node(4)
    root_node.insert(2)
    root_node.insert(1)
    root_node.insert(7)
    root_node.insert(5)
    root_node.insert(6)

    expected = False
    output = root_node.find(3)
    assert output == expected

def test_find_node_in_linked_list_tree():
    root_node = Binary_Tree_Node(1)
    root_node.insert(2)
    root_node.insert(3)
    root_node.insert(4)
    root_node.insert(5)

    expected = True
    output = root_node.find(5)
    assert output == expected

def test_delete_node_one_node_tree(capsys):
    root_node = Binary_Tree_Node(1)
    root_node.delete(1)
    root_node.in_order_print(root_node)

    expected = "None "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_leaf_node_in_full_tree(capsys):
    root_node = Binary_Tree_Node(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.delete(1)
    root_node.in_order_print(root_node)

    expected = "3 4 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_not_in_full_tree(capsys):
    root_node = Binary_Tree_Node(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.delete(12)
    root_node.in_order_print(root_node)

    expected = "1 3 4 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_with_one_left_child(capsys):
    root_node = Binary_Tree_Node(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.delete(3)
    root_node.in_order_print(root_node)

    expected = "1 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_with_one_right_child(capsys):
    root_node = Binary_Tree_Node(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(9)
    root_node.delete(7)
    root_node.in_order_print(root_node)

    expected = "1 3 5 9 "
    output = capsys.readouterr().out
    assert output == expected
