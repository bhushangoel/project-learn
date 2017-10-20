class Stack:
    def __init__(self, limit=10):
        self.list = []
        self.limit = limit

    def isEmpty(self):
        return len(self.list) <= 0

    def pushitem(self, item):
        if len(self.list) >= self.limit:
            print("Stack Overflow")
        else:
            self.list.append(item)

        print("stack after push : ", self.list)

    def popitem(self):
        if len(self.list) <= 0:
            print("Stack underflow")
            return 0
        else:
            return self.list.pop()

    def peek(self):
        if len(self.list) <= 0:
            print("Stack underflow")
            return 0
        else:
            return self.list[-1]

    def size(self):
        return len(self.list)



# our_stack = Stack(5)
# our_stack.push(1)
# our_stack.push(2)
# our_stack.push(3)
# our_stack.push(4)
# print(our_stack.peek())
# our_stack.push(5)
# our_stack.pop()
# our_stack.pop()
# our_stack.push(6)
# our_stack.push(7)