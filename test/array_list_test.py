from src.array_list import Array_List

def test_bubble_sort_empty_list():
    array_list = Array_List()
    array_list.bubble_sort()

    expected = []
    output = array_list.list
    assert output == expected

def test_bubble_sort_one_item_list():
    array_list = Array_List([1])
    array_list.bubble_sort()

    expected = [1]
    output = array_list.list
    assert output == expected

def test_bubble_sort_two_item_list():
    array_list = Array_List([2, 1])
    array_list.bubble_sort()

    expected = [1, 2]
    output = array_list.list
    assert output == expected

def test_bubble_sort_five_elements():
    array_list = Array_List([3, 2, 4, 1, 6])
    array_list.bubble_sort()

    expected = [1, 2, 3, 4, 6]
    output = array_list.list
    assert output == expected

def test_bubble_sort_sorted_array():
    array_list = Array_List([1, 2, 4, 6, 8])
    array_list.bubble_sort()

    expected = [1, 2, 4, 6, 8]
    output = array_list.list
    assert output == expected

def test_binary_search_empty_list():
    array_list = Array_List()

    expected = False
    output = array_list.binary_search(2)
    assert output == expected

def test_binary_search_one_element_not_found():
    array_list = Array_List([1])

    expected = False
    output = array_list.binary_search(2)
    assert output == expected

def test_binary_search_one_element_found():
    array_list = Array_List([1])

    expected = True
    output = array_list.binary_search(1)
    assert output == expected

def test_binary_search_odd_full_list_not_found():
    array_list = Array_List([1, 3, 5, 7, 8])

    expected = False
    output = array_list.binary_search(0)
    assert output == expected

def test_binary_search_odd_full_list_found():
    array_list = Array_List([1, 3, 5, 7, 8])

    expected = True
    output = array_list.binary_search(8)
    assert output == expected

def test_binary_search_even_full_list_not_found():
    array_list = Array_List([1, 3, 5, 8])

    expected = False
    output = array_list.binary_search(2)
    assert output == expected

def test_binary_search_even_full_list_found():
    array_list = Array_List([1, 3, 5, 8])

    expected = True
    output = array_list.binary_search(5)
    assert output == expected
