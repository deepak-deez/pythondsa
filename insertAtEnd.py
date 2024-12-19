from linkedList import Node
def insertAtEnd(self,data):
    newNode = Node()
    newNode.data =data
    current = self.head
    while current.next != None:
        current =current.next
    current.next =newNode
    self.length +=1
    