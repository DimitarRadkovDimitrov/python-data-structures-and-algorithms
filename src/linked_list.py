from .linked_list_node import Linked_List_Node

class Linked_List:
    def __init__(self, value):
        head = Linked_List_Node(value)
        self.head = head

    def print(self):
        head = self.head
        while head:
            print(f"{head.value} -> ", end="")
            head = head.next
        print("NULL")

    def find(self, value_to_find):
        head = self.head
        while head:
            if head.value == value_to_find:
                return True
            head = head.next
        return False

    def add_to_front(self, node_to_add):
        temp = node_to_add
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = node_to_add
