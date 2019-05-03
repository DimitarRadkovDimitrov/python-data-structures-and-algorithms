from src.stack import Stack

def test_print_empty_stack(capsys):
    stack = Stack()
    stack.print()

    expected = "[]\n"
    output = capsys.readouterr().out
    assert output == expected

def test_print_stack_with_elements(capsys):
    stack = Stack([1, 2, 3, 4, 5])
    stack.print()

    expected = "[1, 2, 3, 4, 5]\n"
    output = capsys.readouterr().out
    assert output == expected

def test_peek_empty_stack():
    stack = Stack()
    
    expected = None
    output = stack.peek()
    assert output == expected

def test_peek_stack_with_elements():
    stack = Stack([1, 2, "Dog"])

    expected = "Dog"
    output = stack.peek()
    assert output == expected
    assert stack.stack[-1] == expected

def test_is_empty():
    stack = Stack()

    expected = True
    output = stack.is_empty()
    assert output == expected

def test_is_empty_with_multiple_elements():
    stack = Stack([1, 3, 1])

    expected = False
    output = stack.is_empty()
    assert output == expected

def test_push_empty_stack():
    stack = Stack()
    element = 230
    stack.push(element)

    expected = [230]
    output = stack.stack
    assert output == expected

def test_push_with_multiple_elements():
    stack = Stack()
    stack.push([1, 2, 3])
    stack.push("Horse")
    stack.push(9.321)

    expected = [[1, 2, 3], "Horse", 9.321]
    output = stack.stack
    assert output == expected

def test_pop_with_empty_stack():
    stack = Stack()
    
    expected = None
    output = stack.pop()
    assert output == expected

def test_pop_with_full_stack():
    stack = Stack([2, 4, 1, 4020]) 

    expected = 4020
    output = stack.pop()
    assert output == expected
    assert stack.stack[-1] == 1
