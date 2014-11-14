class Stack:
    data = []
    def push(self, name):
        self.data.append(name)
    def pop(self):
        return self.data.pop()
