#!/usr/local/bin/python3

class Linked_List_Node:
    """ Linked List Class """

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def print(self):
        while self:
            print(f"{self.value} -> ", end="")
            self = self.next
        print("NULL")
