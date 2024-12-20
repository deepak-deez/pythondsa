class circularLinkedList:
    def __init__(self, node =None):
        self.length = 0
        self.head = node

class Node:
    # node of a circular Linked List
    def __init__(self , data = None ,next = None):
        self.data =data
        self.next = next
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    
    def circularListLength(self):
        currentNode = self.head
        if currentNode ==None:
            return 0
        count =1
        currentNode = currentNode.next
        while currentNode!=self.head:
            currentNode = currentNode.next
            count+=1
        return count
    
    def printCircularList(self):
        currentNode =self.head
        if currentNode ==None:
            return 0
        print(currentNode.data)
        while currentNode!= self.head:
            currentNode = currentNode.next
            print(currentNode.data)

    def insertAtBeginningInCLL(self, data):
        currentNode =self.head
        newNode = Node(data)
        if self.head ==None:
            self.head = newNode
        else:
            while currentNode.next!=self.head:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.next = self.head
            self.head = newNode
    
    def deleteLastNodeInCLL(self):
        temp = self.head
        currentNode =self.head
        if self.head ==None:
            print("List is empty")
            return
        while currentNode.next!=self.head:
            temp = currentNode
            currentNode = currentNode.next
        temp.next = currentNode.next
        currentNode.next =None
        return
    
    