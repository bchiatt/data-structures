class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def trav_tree(self, obj):
        if self.data < obj and self.next is None:
            self.next = Node(obj)
            return
        elif self.data < obj:
            self.next.trav_tree(obj)
        elif not (not (self.data > obj) or not (self.prev is None)):
            self.prev = Node(obj)
            return
        else:
            self.prev.trav_tree(obj)

    def order_children(self):
        if self.prev:
            self.prev.order_children()
        print(self.data)
        if self.next:
            self.next.order_children()


class BinaryTree:
    root = None

    def insert(self, obj):
        if self.root is None:
            self.root = Node(obj)
        else:
            self.root.trav_tree(obj)

    def print(self):
        if self.root is None:
            print('the tree is empty')
        else:
            self.root.order_children()

tree = BinaryTree()
tree.print()
tree.insert('greg')
tree.insert('albert')
tree.insert('toby')
tree.insert('ezekiel')
tree.insert('gary')
tree.insert('wanda')
tree.insert('bob')
tree.insert('allen')
tree.insert('thelma')
tree.print()

pass