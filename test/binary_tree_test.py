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
