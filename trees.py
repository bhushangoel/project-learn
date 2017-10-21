from queue import Queue
from stacksimplearray import Stack


class Tree:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def printAllLevelOrder(self):
        if root is None:
            return

        q = Queue(10)
        q.enqueue(root)
        result = []
        node = None
        while not q.isEmpty():
            node = q.dequeue()
            result.append(node.data)
            if node.getLeft():
                q.enqueue(node.getLeft())
            if node.getRight():
                q.enqueue(node.getRight())

        print("tree result : ", result)
        return result


root = Tree(1)

root.left = Tree(2)
root.right = Tree(3)

root.left.left = Tree(4)
root.left.right = Tree(5)

root.right.left = Tree(6)
root.right.right = Tree(7)

root.left.left.left = Tree(11)


# root.left.left.right = Tree(6)
# root.left.left.right.left = Tree(7)


# print(root)
# print(root.printAllLevelOrder())

def deleteNode(root, data):
    if root is None:
        return
    q = Queue()
    node = None
    deep = None
    dleft = None
    dright = None
    result = []
    q.enqueue(root)

    while not q.isEmpty():
        node = q.dequeue()
        result.append(node.data)
        if node.getLeft():
            q.enqueue(node.getLeft())
            if node.getLeft().data == data:
                dleft = node
        if node.getRight():
            q.enqueue(node.getRight())
            if node.getRight().data == data:
                dright = node

    root.printAllLevelOrder()
    deep = node
    if dleft is not None:
        dleft.left = deep
        node.data = data
    elif dright is not None:
        dright.right.data, node.data = deep.data, data

    print("node here : ", deep, deep.data)
    deep = None
    root.printAllLevelOrder()


# deleteNode(root, 3)


def depeestNode(root):
    if root is None:
        return
    q = Queue()
    node = None
    q.enqueue(root)

    while not q.isEmpty():
        node = q.dequeue()
        if node.getLeft():
            q.enqueue(node.getLeft())
        if node.getRight():
            q.enqueue(node.getRight())

    return node.data


# depeestNode(root)

'''
Iterative method
count number of levels in tree and return height accordingly
'''


def getHeight(root):
    if root is None:
        return 0

    q = []
    node = None
    height = 0
    q.append(root)

    while True:
        # number of nodes at current level
        l = len(q)
        if l == 0:
            return height - 1
        height += 1
        while l > 0:
            node = q[0]
            q.pop(0)
            if node.getLeft():
                q.append(node.getLeft())
            if node.getRight():
                q.append(node.getRight())
            l -= 1


# print(getHeight(root))


def insertItem(root, item):
    if root is None:
        root = Tree(item)
        return

    newNode = Tree(item)
    q = Queue()
    node = None
    q.enqueue(root)

    while not q.isEmpty():
        node = q.dequeue()
        # for i in q.queue:
        #     print('i : ', i.data)

        if node.getLeft():
            q.enqueue(node.getLeft())
        else:
            node.left = newNode
            break

        if node.getRight():
            q.enqueue(node.getRight())
        else:
            node.right = newNode
            break

    root.printAllLevelOrder()


# insertItem(root, 5)


def deleteTree(root):
    # print("root 1 : ", root.printAllLevelOrder())
    if root is None:
        return
    # root.printAllLevelOrder()
    deleteTree(root.left)
    deleteTree(root.right)
    root.printAllLevelOrder()
    del root




deleteTree(root)


def reverseTree(root):
    if root is None:
        return

    s = Stack(10)
    q = Queue(10)
    q.enqueue(root)
    node = None
    while not q.isEmpty():
        node = q.dequeue()
        # print("node here : ", node, node.data, node.getLeft())
        print('=====>', node.data)
        if node.getRight():
            q.enqueue(node.getRight())
        if node.getLeft():
            q.enqueue(node.getLeft())

        s.pushitem(node.data)

    print("s : ", s.list)
    while len(s.list) > 0:
        print(s.popitem())


# reverseTree(root)


def preorder(root, result):
    print("1 :", result)
    if not root:
        return
    print('data : ', root.data)
    result.append(root.data)
    preorder(root.left, result)
    preorder(root.right, result)

# arr = []
# preorder(root, arr)
# print('arr : ', arr)
