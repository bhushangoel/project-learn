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

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def getLength(self, l):
        count = 0
        curr = l.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def mergeList(self, l1, l2):
        curr1 = l1.head
        curr2 = l2.head
        curr3 = None
        while True:
            print("-=-=-=-", curr1.data, curr2.data)
            if curr1 or curr2:
                if curr1.data < curr2.data:
                    tmpNode = curr1
                    newNode = curr1.next
                    curr1.next = curr2
                    newNode.next = tmpNode.next
                    curr2 = curr2.next
                    curr1 = newNode.next
                else:
                    tmpNode = curr2
                    newNode = curr2.next
                    curr2.next = curr1
                    newNode.next = tmpNode.next
                    curr1 = curr1.next
                    curr2 = newNode.next
            else:
                break

        print(curr1)

    def compareLists(self, l1, l2):
        if l1.getLength(l1) != l2.getLength(l2):
            return 0
        else:
            curr1 = l1.head
            curr2 = l2.head
            isEqual = True
            while curr1 and curr2:
                if curr1.data != curr2.data:
                    isEqual = False
                    break
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next

            if isEqual:
                return 1
            else:
                return 0


if __name__ == '__main__':
    l1 = LinkedList()
    l1.head = Node(1)
    second = Node(3)
    third = Node(4)

    l1.head.next = second
    second.next = third

    l2 = LinkedList()
    l2.head = Node(2)
    second = Node(5)

    l2.head.next = second

    print("----l1----")
    l1.printList()
    print("----l2----")
    l2.printList()
    print("----merge----")
    l3 = LinkedList()
    l1.mergeList(l1, l2)
    l2.printList()
