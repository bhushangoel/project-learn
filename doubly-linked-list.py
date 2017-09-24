# Doubly Linked List

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize # next as null
        self.prev = None  # Initialize # prev as null


# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def getLength(self):
        templ = self.head
        length = 0
        while templ:
            length += 1
            templ = templ.next
        return length

    # 1. Traverse and print linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, 'curr : ', temp, 'next : ', temp.next, 'prev : ', temp.prev)
            temp = temp.next

    def addInBegining(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            temp.prev = self.head

    def addAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            temp = curr
            curr.next = newNode
            newNode.prev = temp

    def addAtPos(self, data, k):
        l = self.getLength()
        if l <= k:
            return None
        else:
            curr = self.head
            count = 0
            while count < k - 1:
                count += 1
                curr = curr.next
            temp = curr
            newNode = Node(17)
            newNode.prev = temp
            newNode.next = temp.next
            temp.next = newNode
            newNode.next.prev = newNode

    def deleteStart(self):
        l = self.getLength()
        if l == 0:
            return None
        elif l == 1:
            self.head = None
        else:
            curr = self.head
            self.head = curr.next
            self.head.prev = None

    def deleteEnd(self):
        l = self.getLength()
        if l == 0:
            return None
        elif l == 1:
            self.head = None
        else:
            curr = self.head
            tempNode = None
            while curr.next:
                tempNode = curr
                curr = curr.next

            tempNode.next = None


if __name__ == '__main__':
    l = LinkedList()

    first = Node(10)
    l.head = first

    second = Node(20)
    second.prev = first

    third = Node(30)
    third.prev = second

    l.head.next = second
    second.next = third

    l.printList()
    print('--------adding in beginning---------')
    l.addInBegining(5)
    l.printList()
    print('--------adding at end---------')
    l.addAtEnd(22)
    l.printList()
    print('--------adding at nth pos---------')
    l.addAtPos(17, 2)
    l.printList()
    print('--------delete from start---------')
    l.deleteStart()
    l.printList()
    print('--------delete from end---------')
    l.deleteEnd()
    l.printList()
