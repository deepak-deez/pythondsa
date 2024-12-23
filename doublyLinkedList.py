class Node:
    def __init__(self,data =None, next= None , prev =None):
        self.data =data
        self.next =next
        self.prev =prev
    def setData(self,data):
        self.data =data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next =next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    def setPrev(self, prev):
        self.prev =prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev!=None
    def __str__(self):
        return "Node[Data = %s]"% (self.data)
    
    def insertAtBeginning(self,data):
        newNode =Node(data, None, None)
        if self.head ==None:
            self.head =newNode
        else:
            newNode.prev =None
            newNode.next =self.head
            self.head =newNode

    def insertAtEnd(self,data):
        if self.head ==None:
            self.head =Node(data)
        else:
            current =self.head
            while current.next!=None:
                current =current.next
            newNode = Node(data)
            newNode.prev =current
            newNode.next =None

    def getNode(self, index):
        currentNode = self.head
        if currentNode ==None:
            return None
        i=0
        while i<index and currentNode.next is not None:
            currentNode = currentNode.next
            if currentNode ==None:
                break
            i+=1
        return currentNode
    
    def insertAtGivenPosition(self,index,data):
        newNode =Node(data)
        if self.head ==None or index ==0:
            self.insertAtBeginning(data)
        elif index>0:
            temp =self.getNode(index)
            if temp ==None or temp.next==None:
                self.insertAtEnd(data)
            else:
                newNode.next =temp.next
                newNode.prev =temp
                temp.next.prev =newNode
                temp.next =newNode
    
    def deleteFromGivenPosition(self, index):
        temp = self.getNode(index)
        if temp:
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            temp.prev =None
            temp.next =None
            temp.data = None
    
    def deleteWithData(self,data):
        temp =self.head
        while temp is not None:
            if temp.data == data:
                if temp.next is not None:
                    temp.prev.next =temp.next
                    temp.next.prev =temp.prev
                else:
                    self.head = temp.next
                    temp.next.prev = None
                temp = temp.next