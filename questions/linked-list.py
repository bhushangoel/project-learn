# Circular Linked List

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def getLength(self):
        templ = self.head
        length = 0
        while templ != self.head:
            length += 1
            templ = templ.next
        return length

    # 1. Traverse and print linked list
    def printList(self):
        curr = self.head
        while curr.next:
            print(curr.data, curr.next)
            curr = curr.next
            if curr == self.head:
                break

    # insert at beginning
    def addStart(self, data):
        fourth = Node(data)
        if self.head == None:
            self.head = fourth
        else:
            curr = self.head
            fourth.next = curr
            temp = None
            while curr.next:
                temp = curr
                curr = curr.next
                if curr == self.head:
                    break

            self.head = fourth
            temp.next = fourth

    def addEnd(self, data):
        fifth = Node(data)
        curr = self.head
        if curr == None:
            curr = fifth
        while curr.next != None:
            curr = curr.next
        curr.next = fifth

    def addAtNthPos(self, data, k):
        length = self.getLength()

        if k < length:
            newNode = Node(data)
            curr = self.head
            count = 0
            while count < k - 1:
                count += 1
                curr = curr.next

            temp = curr.next
            curr.next = newNode
            newNode.next = temp

    def addAtSortedPos(self, data):
        l3 = Node(data)
        curr = self.head
        tempNode = None
        while curr.data < data:
            tempNode = curr
            curr = curr.next

        temp = tempNode.next
        tempNode.next = l3
        l3.next = temp

    def deleteFromBegining(self):
        length = self.getLength()

        if length == 0:
            return "List is empty"
        else:
            curr = self.head
            self.head = curr.next

    def deleteFromEnd(self):
        length = self.getLength()

        if length == 0:
            return "List is empty"
        else:
            curr = self.head
            tempNode = None
            while curr.next:
                tempNode = curr
                curr = curr.next

            tempNode.next = None

    def searchItem(self, item):
        curr = self.head
        found = False

        while curr.next:
            if curr.data == item:
                found = True
            curr = curr.next
        print('found : ', found)

    def reverse(self):
        curr = self.head
        prev = None
        while curr.next:
            tempNode = curr.next
            curr.next = prev
            prev = curr
            curr = tempNode

        self.head = curr
        self.head.next = prev


if __name__ == '__main__':
    l = LinkedList()

    first = Node(10)
    l.head = first
    second = Node(20)
    third = Node(30)

    l.head.next = second
    second.next = third
    third.next = first

    l.printList()
    print('--------adding in beginning---------')
    l.addStart(5)
    l.printList()
