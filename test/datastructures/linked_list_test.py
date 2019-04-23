from src.datastructures.linked_list import LinkedList, LinkedListNode

def test_print_empty_list(capsys):
    linked_list = LinkedList()
    linked_list.print()

    expected = "NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_print_list_with_one_element(capsys):
    linked_list_node = LinkedListNode(1)
    linked_list = LinkedList(linked_list_node)
    linked_list.print()

    expected = "1 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_print_list_with_multiple_elements(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3
    linked_list.print()

    expected = "1 -> 2 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_find_in_empty_list():
    linked_list = LinkedList()
    
    expected = False
    output = linked_list.find(1)
    assert output == expected

def test_find_not_in_list():  
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3

    expected = False
    output = linked_list.find(4)
    assert output == expected

def test_find_in_list():
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3

    expected = True
    output = linked_list.find(3)
    assert output == expected

def test_add_to_front_to_empty_list(capsys):
    linked_list = LinkedList()
    node_to_add = LinkedListNode(1)
    linked_list.add_to_front(node_to_add)
    linked_list.print()

    expected = "1 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_front_one_element(capsys):
    node_1 = LinkedListNode(1)
    node_3 = LinkedListNode(3)
    node_to_add = LinkedListNode(2)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_3    
    linked_list.add_to_front(node_to_add)
    linked_list.print()

    expected = "2 -> 1 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_front_one_list(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2

    node_to_add = LinkedListNode(3)
    node_4 = LinkedListNode(4)
    node_5 = LinkedListNode(5)
    node_to_add.next = node_4
    node_4.next = node_5
    
    linked_list.add_to_front(node_to_add)
    linked_list.print()

    expected = "3 -> 4 -> 5 -> 1 -> 2 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_back_to_empty_list(capsys):
    linked_list = LinkedList()
    node_to_add = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_to_add.next = node_2

    linked_list.add_to_back(node_to_add)
    linked_list.print()

    expected = "1 -> 2 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_back_one_element(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2

    linked_list.add_to_back(node_3)
    linked_list.print()

    expected = "1 -> 2 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_add_to_back_one_list(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    node_4 = LinkedListNode(4)
    node_5 = LinkedListNode(5)

    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_3.next = node_4
    node_4.next = node_5

    linked_list.add_to_back(node_3)
    linked_list.print()

    expected = "1 -> 2 -> 3 -> 4 -> 5 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_from_empty_list(capsys):
    linked_list = LinkedList()
    linked_list.remove(7)
    linked_list.print()

    expected = "NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_from_one_element_list(capsys):
    node_1 = LinkedListNode(1)
    linked_list = LinkedList(node_1)
    linked_list.remove(1)
    linked_list.print()

    expected = "NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_not_in_list(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3
    linked_list.remove(7)
    linked_list.print()

    expected = "1 -> 2 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_element_at_head(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3
    linked_list.remove(1)
    linked_list.print()

    expected = "2 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_element_at_middle(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3
    linked_list.remove(2)
    linked_list.print()

    expected = "1 -> 3 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected

def test_remove_element_at_tail(capsys):
    node_1 = LinkedListNode(1)
    node_2 = LinkedListNode(2)
    node_3 = LinkedListNode(3)
    linked_list = LinkedList(node_1)
    linked_list.head.next = node_2
    node_2.next = node_3
    linked_list.remove(3)
    linked_list.print()

    expected = "1 -> 2 -> NULL\n"
    output = capsys.readouterr().out
    assert output == expected
