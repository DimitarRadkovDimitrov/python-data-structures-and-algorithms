class Array_List:
    def __init__(self, initial_list=None):
        if initial_list:
            self.list = initial_list
        else:
            self.list = []
    
    def bubble_sort(self):
        for i in range(len(self.list)):
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[i]:
                    self.swap(j, i)
    
    def swap(self, index_of_first_number, index_of_second_number):
        temp = self.list[index_of_first_number]
        self.list[index_of_first_number] = self.list[index_of_second_number]
        self.list[index_of_second_number] = temp

    def binary_search(self, value_to_search):
        lower_bound = 0
        higher_bound = len(self.list) - 1

        while lower_bound <= higher_bound:
            middle = (lower_bound + higher_bound) // 2
            if value_to_search < self.list[middle]:
                higher_bound = middle - 1
            elif value_to_search > self.list[middle]:
                lower_bound = middle + 1
            else:
                return True
        return False
