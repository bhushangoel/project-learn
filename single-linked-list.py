# Single Linked List

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
        while templ:
            length += 1
            templ = templ.next
        return length

    # 1. Traverse and print linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, temp.next)
            temp = temp.next

    # insert at beginning
    def addStart(self, data):
        fourth = Node(data)
        if self.head == None:
            self.head = fourth
        else:
            temp = self.head
            self.head = fourth
            self.head.next = temp

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
            curr.next = prev
            prev = curr
            curr = next

        self.head = curr


if __name__ == '__main__':
    l = LinkedList()

    first = Node(10)
    l.head = first
    second = Node(20)
    third = Node(30)

    l.head.next = second
    second.next = third

    l.printList()
    print('--------adding in beginning---------')
    l.addStart(7)
    l.printList()
    print('--------adding at end---------')
    l.addEnd(32)
    l.printList()
    print('--------adding at nth pos---------')
    l.addAtNthPos(15, 2)
    l.printList()
    print('--------adding at sorted pos---------')
    l.addAtSortedPos(22)
    l.printList()
    print('--------delete from beginning---------')
    l.deleteFromBegining()
    l.printList()
    print('--------delete from end---------')
    l.deleteFromEnd()
    l.printList()
    print('--------search item---------')
    l.searchItem(23)
    l.printList()
