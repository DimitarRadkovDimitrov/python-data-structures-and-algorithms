from src.queue import Queue

def test_print_empty_queue(capsys):
    queue = Queue()
    queue.print()

    expected = "[]\n"
    output = capsys.readouterr().out
    assert output == expected

def test_print_queue_with_elements(capsys):
    queue = Queue([1, 2, 3, 4, 5])
    queue.print()

    expected = "[1, 2, 3, 4, 5]\n"
    output = capsys.readouterr().out
    assert output == expected

def test_peek_empty_queue():
    queue = Queue()
    
    expected = None
    output = queue.peek()
    assert output == expected

def test_peek_queue_with_elements():
    queue = Queue([1, 2, "Dog"])

    expected = 1
    output = queue.peek()
    assert output == expected
    assert queue.queue[0] == expected

def test_is_empty():
    queue = Queue()

    expected = True
    output = queue.is_empty()
    assert output == expected

def test_is_empty_with_multiple_elements():
    queue = Queue([1, 3, 1])

    expected = False
    output = queue.is_empty()
    assert output == expected

def test_enqueue_empty_queue():
    queue = Queue()
    element = 230
    queue.enqueue(element)

    expected = [230]
    output = queue.queue
    assert output == expected

def test_enqueue_with_multiple_elements():
    queue = Queue()
    queue.enqueue([1, 2, 3])
    queue.enqueue("Horse")
    queue.enqueue(9.321)

    expected = [[1, 2, 3], "Horse", 9.321]
    output = queue.queue
    assert output == expected

def test_dequeue_with_empty_queue():
    queue = Queue()
    
    expected = None
    output = queue.dequeue()
    assert output == expected

def test_dequeue_with_single_element_queue():
    queue = Queue([2]) 

    expected = 2
    output = queue.dequeue()
    assert output == expected
    assert len(queue.queue) == 0

def test_dequeue_with_full_queue():
    queue = Queue([2, 4, 1, 4020]) 

    expected = 2
    output = queue.dequeue()
    assert output == expected
    assert queue.queue[0] == 4
