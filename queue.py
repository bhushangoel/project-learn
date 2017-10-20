from stacksimplearray import Stack


class Queue:
    def __init__(self, limit=5):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enqueue(self, item):
        if self.size >= self.limit:
            # print("---Queue overflow---")
            self.resize()

        self.queue.append(item)

        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        # print("Queue after enqueue : ", self.queue)

    def dequeue(self):
        if self.size <= 0:
            print("---Queue underflow---")
        else:
            a = self.queue.pop(0)
            self.size -= 1

            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            # print("Queue after dequeue : ", self.queue)
            return a

    def queuerear(self):
        if self.rear == None:
            print("Queue is empty")
        else:
            print("Queue Rear : ", self.queue[self.rear])
            return self.queue[self.rear]

    def queuefront(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Queue Front : ", self.queue[self.front])
            return self.queue[self.front]

    def queuesize(self):
        print("Queue size : ", self.size)
        return self.size

    def resize(self):
        newqueue = list(self.queue)
        self.limit = 2 * self.limit
        self.queue = newqueue

    def reverse(self):
        my_stack = Stack(self.queuesize())
        while self.queuesize() > 0:
            i = self.dequeue()
            my_stack.pushitem(i)

        while len(my_stack.list) > 0:
            j = my_stack.popitem()
            self.enqueue(j)
        return self.queue



# my_queue = Queue()
# print("Queue is empty ? ", my_queue.isEmpty())
# my_queue.enqueue('A')
# my_queue.enqueue('B')
# my_queue.enqueue('C')
# my_queue.dequeue()
# my_queue.queuerear()
# print("Queue is empty ? ", my_queue.isEmpty())
# my_queue.enqueue('D')
# my_queue.enqueue('E')
# my_queue.enqueue('F')
# my_queue.enqueue('G')
# my_queue.queuefront()
# my_queue.queuesize()
# print("reverse : ", my_queue.reverse())
