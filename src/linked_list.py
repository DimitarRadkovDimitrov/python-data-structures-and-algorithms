class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
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

    def add_to_back(self, node_to_add):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node_to_add
        else:
            self.head = node_to_add

    def remove(self, value_to_remove):
        curr = self.head
        prev = None

        while curr:
            if curr.value == value_to_remove:
                if prev:
                    prev.next = curr.next
                    del curr
                else:
                    temp = curr
                    curr = curr.next
                    self.head = curr
                    del temp
                return
            prev = curr
            curr = curr.next
