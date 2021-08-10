class Stack:
    def __init__(self):
        self.l=[]
    def push(self, val):
        self.l.append(val)
    def pop(self):
        return self.l.pop()
    def peek(self):
        return self.l[-1]
    def list_print(self):
        print(self.l)


s=Stack()
s.push(12)
s.push(5)
s.push(25)
s.list_print()