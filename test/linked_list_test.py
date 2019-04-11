from src.linked_list import Linked_List_Node
from src.linked_list import Linked_List

def test_print_list_with_one_element(capsys):
    expected = "1 -> NULL\n"
    linked_list = Linked_List(1)
    linked_list.print()
    output = capsys.readouterr().out
    assert output == expected

def test_print_list_with_multiple_elements(capsys):
    expected = "1 -> 2 -> 3 -> NULL\n"
    linked_list = Linked_List(1)
    node2 = Linked_List_Node(2)
    node3 = Linked_List_Node(3)
    linked_list.head.next = node2
    node2.next = node3
    linked_list.print()
    output = capsys.readouterr().out
    assert output == expected

def test_find_not_in_list():
    expected = False
    linked_list = Linked_List(1)
    node2 = Linked_List_Node(2)
    node3 = Linked_List_Node(3)
    linked_list.head.next = node2
    node2.next = node3
    output = linked_list.find(4)
    assert output == expected

def test_find_in_list():
    expected = True
    linked_list = Linked_List(1)
    node2 = Linked_List_Node(2)
    node3 = Linked_List_Node(3)
    linked_list.head.next = node2
    node2.next = node3
    output = linked_list.find(3)
    assert output == expected

def test_add_to_front_one_element(capsys):
    expected = "2 -> 1 -> 3 -> NULL\n"
    linked_list = Linked_List(1)
    node2 = Linked_List_Node(3)
    linked_list.head.next = node2
    node_to_add = Linked_List_Node(2)
    linked_list.add_to_front(node_to_add)
    linked_list.print()
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_front_one_list(capsys):
    node_to_add = Linked_List_Node(3)
    node_4 = Linked_List_Node(4)
    node_5 = Linked_List_Node(5)
    node_to_add.next = node_4
    node_4.next = node_5
    
    linked_list = Linked_List(1)
    node_2 = Linked_List_Node(2)
    linked_list.head.next = node_2
    
    linked_list.add_to_front(node_to_add)
    linked_list.print()
    expected = "3 -> 4 -> 5 -> 1 -> 2 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected
