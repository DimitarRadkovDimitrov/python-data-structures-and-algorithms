class Trie:
    def __init__(self, value='*'):
        self.value = value
        self.children = {}

    def get_words(self, root):
        word_list = []
        for key, child in root.children.items():
            if child.children:
                for end_of_word in self.get_words(child):                
                    word_list.append(key + end_of_word)
            else:
                word_list.append(key)                
        return word_list
    
    def insert(self, string_to_insert):
        temp = self
        for letter in string_to_insert:
            if letter not in temp.children:
                trie_to_insert = Trie(letter)
                temp.children[letter] = trie_to_insert
            temp = temp.children[letter]
