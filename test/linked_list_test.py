from src.linked_list import Linked_List_Node

def test_print_list_with_one_element(capsys):
    expected = "1 -> NULL\n"
    node = Linked_List_Node(1)
    node.print()
    output = capsys.readouterr().out
    assert output == expected

def test_print_list_with_multiple_elements(capsys):
    expected = "1 -> 2 -> 3 -> NULL\n"
    head = Linked_List_Node(1)
    node2 = Linked_List_Node(2)
    node3 = Linked_List_Node(3)
    head.next = node2
    node2.next = node3
    head.print()
    output = capsys.readouterr().out
    assert output == expected
