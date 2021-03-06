from src.binary_tree import BinaryTree

def test_in_order_print_one_node(capsys):
    root_node = BinaryTree(1)
    root_node.in_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_in_order_print_multiple_nodes(capsys):
    root_node = BinaryTree(4)
    root_node.left_child = BinaryTree(1)
    root_node.left_child.left_child = BinaryTree(7)
    root_node.left_child.right_child = BinaryTree(9)
    root_node.right_child = BinaryTree(5)
    root_node.right_child.left_child = BinaryTree(2)
    root_node.right_child.right_child = BinaryTree(6)
    root_node.in_order_print(root_node)

    expected = "7 1 9 4 2 5 6 "
    output = capsys.readouterr().out
    assert output == expected

def test_pre_order_print_one_node(capsys):
    root_node = BinaryTree(1)
    root_node.pre_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_pre_order_print_multiple_nodes(capsys):
    root_node = BinaryTree(4)
    root_node.left_child = BinaryTree(1)
    root_node.left_child.left_child = BinaryTree(7)
    root_node.left_child.right_child = BinaryTree(9)
    root_node.right_child = BinaryTree(5)
    root_node.right_child.left_child = BinaryTree(2)
    root_node.right_child.right_child = BinaryTree(6)
    root_node.pre_order_print(root_node)

    expected = "4 1 7 9 5 2 6 "
    output = capsys.readouterr().out
    assert output == expected

def test_post_order_print_one_node(capsys):
    root_node = BinaryTree(1)
    root_node.post_order_print(root_node)

    expected = "1 "
    output = capsys.readouterr().out
    assert output == expected

def test_post_order_print_multiple_nodes(capsys):
    root_node = BinaryTree(4)
    root_node.left_child = BinaryTree(1)
    root_node.left_child.left_child = BinaryTree(7)
    root_node.left_child.right_child = BinaryTree(9)
    root_node.right_child = BinaryTree(5)
    root_node.right_child.left_child = BinaryTree(2)
    root_node.right_child.right_child = BinaryTree(6)
    root_node.post_order_print(root_node)

    expected = "7 9 1 2 6 5 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_one_node(capsys):
    root_node = BinaryTree(4)
    root_node.insert(2)
    root_node.in_order_print(root_node)
    
    expected = "2 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_same_node_twice(capsys):
    root_node = BinaryTree(4)
    root_node.insert(2)
    root_node.insert(2)
    root_node.in_order_print(root_node)

    expected = "2 4 "
    output = capsys.readouterr().out
    assert output == expected

def test_insert_multiple_nodes(capsys):
    root_node = BinaryTree(4)
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
    root_node = BinaryTree(1)
    root_node.insert(3)
    root_node.insert(5)
    root_node.insert(7)
    root_node.in_order_print(root_node)

    expected = "1 3 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_find_node_in_one_node_tree():
    root_node = BinaryTree(7)
    
    expected = True
    output = root_node.find(7)
    assert output == expected

def test_find_node_not_in_one_node_tree():
    root_node = BinaryTree(7)
    
    expected = False
    output = root_node.find(1)
    assert output == expected

def test_find_node_in_full_tree():
    root_node = BinaryTree(4)
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
    root_node = BinaryTree(4)
    root_node.insert(2)
    root_node.insert(1)
    root_node.insert(7)
    root_node.insert(5)
    root_node.insert(6)

    expected = False
    output = root_node.find(3)
    assert output == expected

def test_find_node_in_linked_list_tree():
    root_node = BinaryTree(1)
    root_node.insert(2)
    root_node.insert(3)
    root_node.insert(4)
    root_node.insert(5)

    expected = True
    output = root_node.find(5)
    assert output == expected

def test_delete_leaf_node_in_full_tree(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.delete(root_node, 1)
    root_node.in_order_print(root_node)

    expected = "3 4 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_not_in_full_tree(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.delete(root_node, 12)
    root_node.in_order_print(root_node)

    expected = "1 3 4 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_with_one_left_child(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.delete(root_node, 3)
    root_node.in_order_print(root_node)

    expected = "1 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_with_one_right_child(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(9)
    root_node.delete(root_node, 7)
    root_node.in_order_print(root_node)

    expected = "1 3 5 9 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_node_with_two_children(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.delete(root_node, 3)
    root_node.in_order_print(root_node)

    expected = "1 4 5 7 "
    output = capsys.readouterr().out
    assert output == expected

def test_delete_root_node_with_full_tree(capsys):
    root_node = BinaryTree(5)
    root_node.insert(3)
    root_node.insert(7)
    root_node.insert(1)
    root_node.insert(4)
    root_node.insert(3)
    root_node.insert(6)
    root_node.insert(12)
    root_node.insert(10)
    root_node.delete(root_node, 5)
    root_node.in_order_print(root_node)

    expected = "1 3 4 6 7 10 12 "
    output = capsys.readouterr().out
    assert output == expected
