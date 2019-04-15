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
