# Stack data structure
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

#pops(takes out) top element of stack
myStack.pop()

#prints entire stack
print(myStack.get_stack())

#peek checks the top of the stack then returns
print(myStack.peek())