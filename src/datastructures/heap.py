class Heap:
    def __init__(self, from_list=None):
        self.heap = [0]
        if from_list:
            self.heap.extend(from_list)
            self.heapify()

    def heapify(self):
        if len(self.heap) > 2:
            current_sub_heap_index = (len(self.heap) - 1) // 2
            while current_sub_heap_index > 0:
                self.down_heap(current_sub_heap_index)
                current_sub_heap_index = current_sub_heap_index - 1

    def down_heap(self, root_index):
        while root_index * 2 < len(self.heap):
            left_child_index = root_index * 2
            right_child_index = (root_index * 2) + 1

            if right_child_index > len(self.heap) - 1:
                index_of_largest_child = left_child_index
            else:
                if self.heap[right_child_index] > self.heap[left_child_index]:
                    index_of_largest_child = right_child_index
                else:
                    index_of_largest_child = left_child_index
            
            if self.heap[root_index] < self.heap[index_of_largest_child]:
                self.swap(root_index, index_of_largest_child)
                root_index = index_of_largest_child
            else:
                break

    def swap(self, index_of_first_number, index_of_second_number):
        temp = self.heap[index_of_first_number]
        self.heap[index_of_first_number] = self.heap[index_of_second_number]
        self.heap[index_of_second_number] = temp

    def insert(self, value_to_insert):
        if value_to_insert:
            self.heap.append(value_to_insert)
            starting_index = len(self.heap) - 1
            self.up_heap(starting_index)
    
    def up_heap(self, root_index):
        while root_index > 1:
            parent_index = root_index // 2
            if self.heap[root_index] > self.heap[parent_index]:
                self.swap(root_index, parent_index)
                root_index = parent_index
            else:
                break

    def heap_sort(self):
        sorted_list = []
        while len(self.heap) > 1:
            max_node = self.delete()
            sorted_list.insert(0, max_node)
        return sorted_list

    def delete(self):
        if len(self.heap) > 1:
            root_index = 1
            temp = self.heap[root_index]
            index_of_last_node = len(self.heap) - 1

            self.swap(root_index, index_of_last_node)
            del self.heap[index_of_last_node]
            self.down_heap(root_index)

            return temp
