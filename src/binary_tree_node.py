class Binary_Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left_child)
            print(f"{node.value} ", end="")
            self.in_order_print(node.right_child)

    def pre_order_print(self, node):
        if node:
            print(f"{node.value} ", end="")
            self.pre_order_print(node.left_child)
            self.pre_order_print(node.right_child)

    def post_order_print(self, node):
        if node:
            self.post_order_print(node.left_child)
            self.post_order_print(node.right_child)
            print(f"{node.value} ", end="")

    def insert(self, value_to_insert):
        if value_to_insert < self.value:
            if self.left_child:
                self.left_child.insert(value_to_insert)
            else:
                self.left_child = Binary_Tree_Node(value_to_insert)
        elif value_to_insert > self.value:
            if self.right_child:
                self.right_child.insert(value_to_insert)
            else:
                self.right_child = Binary_Tree_Node(value_to_insert)

    def find(self, value_to_find):
        if value_to_find < self.value:
            if self.left_child:
                return self.left_child.find(value_to_find)
            else:
                return False
        elif value_to_find > self.value:
            if self.right_child:
                return self.right_child.find(value_to_find)
            else:
                return False
        else:
            return True

    def delete(self, node, value_to_delete):
        if node:
            if value_to_delete < node.value:
                node.left_child = self.delete(node.left_child, value_to_delete)
            elif value_to_delete > node.value:
                node.right_child = self.delete(node.right_child, value_to_delete)
            else:
                if node.left_child and node.right_child:
                    temp = self.get_in_order_successor(node.right_child)
                    node.value = temp.value
                    node.right_child = self.delete(node.right_child, temp.value)
                    return node
                elif node.left_child and node.right_child is None:
                    temp = node.left_child
                    node = None
                    return temp
                elif node.right_child and node.left_child is None:
                    temp = node.right_child
                    node = None
                    return temp
                else:
                    temp = None
                    return temp
        return node

    def get_in_order_successor(self, node):
        while node.left_child:
            node = node.left_child
        return node
