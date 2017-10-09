class Stack:
    def __init__(self, limit=10):
        self.stk = limit * []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print("Stack after push : ", self.stk)

    def resize(self):
        print("resize called")
        newStk = list(self.stk)
        print("newstak1 == ", newStk)
        self.limit = 2 * self.limit
        print("limit : ", self.limit)
        self.stk = newStk
        print("self stk = ", self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack underflow")
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)


our_stack = Stack(10)

our_stack.push(1)
our_stack.push(2)
our_stack.push(3)
our_stack.push(4)
