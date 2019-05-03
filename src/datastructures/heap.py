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
                print(current_sub_heap_index)
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
