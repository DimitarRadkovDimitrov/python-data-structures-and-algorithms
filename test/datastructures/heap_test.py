from src.datastructures.heap import Heap

def test_initialize_empty_heap():
    heap = Heap()

    expected = [0]
    output = heap.heap
    assert output == expected

def test_heapify_empty_list():
    list_to_heapify = []
    heap = Heap(list_to_heapify)

    expected = [0]
    output = heap.heap
    assert output == expected

def test_heapify_list_with_two_elements():
    list_to_heapify = [1, 3]
    heap = Heap(list_to_heapify)
    
    expected = [0, 3, 1]
    output = heap.heap
    assert output == expected

def test_heapify_full_list():
    list_to_heapify = [3, 1, 7, 4]
    heap = Heap(list_to_heapify)
    
    expected = [0, 7, 4, 3, 1]
    output = heap.heap
    assert output == expected

def test_heapify_larger_list():
    list_to_heapify = [1, 9, 7, 4, 3, 8]
    heap = Heap(list_to_heapify)
    
    expected = [0, 9, 4, 8, 1, 3, 7]
    output = heap.heap
    assert output == expected

def test_heapify_heap_list():
    list_to_heapify = [9, 4, 8, 1, 3, 7]
    heap = Heap(list_to_heapify)
    
    expected = [0, 9, 4, 8, 1, 3, 7]
    output = heap.heap
    assert output == expected
