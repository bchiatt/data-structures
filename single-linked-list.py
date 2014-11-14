class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def set_next(self, obj):
        if self.next is None:
            self.next = Node(obj)
            return
        else:
            self.next.set_next(obj)


class SingleLinkedList:
    head = None

    def insert(self, obj):
        if self.head is None:
            self.head = Node(obj)
        else:
            self.head.set_next(obj)


people = SingleLinkedList()
people.insert('bob')
people.insert('sue')
people.insert('sara')

pass