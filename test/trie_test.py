from src.trie import Trie

def test_get_words_one_word():
    root_node = Trie()
    trie_1 = Trie('C')
    trie_2 = Trie('A')
    trie_3 = Trie('R')
    root_node.children[trie_1.value] = trie_1
    trie_1.children[trie_2.value] = trie_2
    trie_2.children[trie_3.value] = trie_3

    expected = ['CAR']
    output = root_node.get_words(root_node)
    assert output == expected

def test_get_words_multiple_words():
    root_node = Trie()
    trie_L1_1 = Trie('A')
    trie_L1_2 = Trie('B')
    trie_L1_3 = Trie('C')

    trie_L2_1 = Trie('T')
    trie_L2_2 = Trie('R')    
    trie_L2_3 = Trie('A')
    trie_L2_4 = Trie('N')
    trie_L2_5 = Trie('E')

    root_node.children[trie_L1_1.value] = trie_L1_1
    root_node.children[trie_L1_2.value] = trie_L1_2
    root_node.children[trie_L1_3.value] = trie_L1_3
    trie_L1_1.children[trie_L2_1.value] = trie_L2_1
    trie_L1_1.children[trie_L2_2.value] = trie_L2_2
    trie_L1_2.children[trie_L2_3.value] = trie_L2_3
    trie_L1_3.children[trie_L2_4.value] = trie_L2_4
    trie_L1_3.children[trie_L2_5.value] = trie_L2_5

    expected = ['AT', 'AR', 'BA', 'CN', 'CE']
    output = root_node.get_words(root_node)
    assert output == expected

def test_get_words_multiple_words_complex():
    root_node = Trie()
    trie_L1_1 = Trie('B')
    trie_L1_2 = Trie('S')
    trie_L2_1 = Trie('E')
    trie_L2_2 = Trie('I')    
    trie_L2_3 = Trie('U')
    trie_L2_4 = Trie('E')
    trie_L2_5 = Trie('T')
    trie_L3_1 = Trie('A')
    trie_L3_2 = Trie('L')    
    trie_L3_3 = Trie('D')
    trie_L3_4 = Trie('L')
    trie_L3_5 = Trie('Y')
    trie_L3_6 = Trie('L')
    trie_L3_7 = Trie('O')
    trie_L4_1 = Trie('R')
    trie_L4_2 = Trie('L')    
    trie_L4_3 = Trie('L')
    trie_L4_4 = Trie('L')
    trie_L4_5 = Trie('C')
    trie_L4_6 = Trie('P')
    trie_L5_1 = Trie('K')

    root_node.children[trie_L1_1.value] = trie_L1_1
    root_node.children[trie_L1_2.value] = trie_L1_2
    trie_L1_1.children[trie_L2_1.value] = trie_L2_1
    trie_L1_1.children[trie_L2_2.value] = trie_L2_2
    trie_L1_1.children[trie_L2_3.value] = trie_L2_3
    trie_L1_2.children[trie_L2_4.value] = trie_L2_4
    trie_L1_2.children[trie_L2_5.value] = trie_L2_5
    trie_L2_1.children[trie_L3_1.value] = trie_L3_1
    trie_L2_1.children[trie_L3_2.value] = trie_L3_2
    trie_L2_2.children[trie_L3_3.value] = trie_L3_3
    trie_L2_3.children[trie_L3_4.value] = trie_L3_4
    trie_L2_3.children[trie_L3_5.value] = trie_L3_5
    trie_L2_4.children[trie_L3_6.value] = trie_L3_6
    trie_L2_5.children[trie_L3_7.value] = trie_L3_7
    trie_L3_1.children[trie_L4_1.value] = trie_L4_1
    trie_L3_2.children[trie_L4_2.value] = trie_L4_2
    trie_L3_4.children[trie_L4_3.value] = trie_L4_3
    trie_L3_6.children[trie_L4_4.value] = trie_L4_4
    trie_L3_7.children[trie_L4_5.value] = trie_L4_5
    trie_L3_7.children[trie_L4_6.value] = trie_L4_6
    trie_L4_5.children[trie_L5_1.value] = trie_L5_1

    expected = ['BEAR', 'BELL', 'BID', 'BULL', 'BUY', 'SELL', 'STOCK', 'STOP']
    output = root_node.get_words(root_node)
    assert output == expected

def test_insert_one_word():
    root_node = Trie()
    root_node.insert("Dimitar")

    expected = ['Dimitar']
    output = root_node.get_words(root_node)
    assert output == expected

def test_insert_same_word_twice():
    root_node = Trie()
    root_node.insert("Dimitar")
    root_node.insert("Dimitar")

    expected = ['Dimitar']
    output = root_node.get_words(root_node)
    assert output == expected

def test_insert_same_word_different_case():
    root_node = Trie()
    root_node.insert("dimitar")
    root_node.insert("DIMITAR")

    expected = ['dimitar', 'DIMITAR']
    output = root_node.get_words(root_node)
    assert output == expected

def test_insert_multiple_words():
    root_node = Trie()
    root_node.insert('BEAR')
    root_node.insert('BELL')
    root_node.insert('BID')
    root_node.insert('BULL')
    root_node.insert('BUY')
    root_node.insert('SELL')
    root_node.insert('STOCK')
    root_node.insert('STOP')

    expected = ['BEAR', 'BELL', 'BID', 'BULL', 'BUY', 'SELL', 'STOCK', 'STOP']
    output = root_node.get_words(root_node)
    assert output == expected

def test_search_empty_trie():
    root_node = Trie()

    expected = False
    output = root_node.search("Dog")
    assert output == expected

def test_search_blank_empty_trie():
    root_node = Trie()

    expected = False
    output = root_node.search('')
    assert output == expected

def test_search_basic_with_multiple_words():
    root_node = Trie()
    root_node.insert('BEAR')
    root_node.insert('BELL')
    root_node.insert('BID')
    root_node.insert('BULL')
    root_node.insert('BUY')
    root_node.insert('SELL')
    root_node.insert('STOCK')
    root_node.insert('STOP')

    expected = True
    output = root_node.search('BULL')
    assert output == expected

def test_search_match_with_different_case():
    root_node = Trie()
    root_node.insert("dimitar")

    expected = False
    output = root_node.search("DIMITAR")
    assert output == expected

def test_search_match_of_suffix():
    root_node = Trie()
    root_node.insert("TESTED")

    expected = True
    output = root_node.search("TEST")
    assert output == expected

def test_search_word_longer_than_match():
    root_node = Trie()
    root_node.insert("TEST")

    expected = False
    output = root_node.search("TESTED")
    assert output == expected
