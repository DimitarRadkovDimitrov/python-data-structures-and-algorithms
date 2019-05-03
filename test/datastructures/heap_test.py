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

def test_insert_empty_heap():
    heap = Heap()
    heap.insert(4)

    expected = [0, 4]
    output = heap.heap
    assert output == expected

def test_insert_empty_heap_two_elements():
    heap = Heap()
    heap.insert(1)
    heap.insert(3)

    expected = [0, 3, 1]
    output = heap.heap
    assert output == expected

def test_insert_into_heap():
    heap = Heap([8, 5, 2, 4, 3, 1])
    heap.insert(6)

    expected = [0, 8, 5, 6, 4, 3, 1, 2]
    output = heap.heap
    assert output == expected

def test_delete_from_empty_heap():
    heap = Heap()
    heap.delete()

    expected = [0]
    output = heap.heap
    assert output == expected

def test_delete_from_one_element_heap():
    heap = Heap([1])
    heap.delete()

    expected = [0]
    output = heap.heap
    assert output == expected

def test_delete_from_two_element_heap():
    heap = Heap([5, 1])
    deleted_node = heap.delete()

    expected = [0, 1]
    output = heap.heap
    assert output == expected
    assert deleted_node == 5

def test_delete_from_full_heap():
    heap = Heap([9, 7, 5, 6, 2])
    deleted_node = heap.delete()

    expected = [0, 7, 6, 5, 2]
    output = heap.heap
    assert output == expected
    assert deleted_node == 9

def test_heap_sort_empty_heap():
    heap = Heap()

    expected = []
    output = heap.heap_sort()
    assert output == expected

def test_heap_sort_one_element_heap():
    heap = Heap([9])

    expected = [9]
    output = heap.heap_sort()
    assert output == expected

def test_heap_sort_with_already_sorted():
    heap = Heap([1, 3, 4, 7, 8, 9])
    
    expected = [1, 3, 4, 7, 8, 9]
    output = heap.heap_sort()
    assert output == expected

def test_heap_sort_with_full_heap():
    heap = Heap([9, 4, 8, 1, 3, 7])
    
    expected = [1, 3, 4, 7, 8, 9]
    output = heap.heap_sort()
    assert output == expected

def test_heap_sort_with_heap_construction():
    heap = Heap([1, 9, 7, 4, 3, 8])
    
    expected = [1, 3, 4, 7, 8, 9]
    output = heap.heap_sort()
    assert output == expected
