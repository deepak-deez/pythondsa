def deleteLastNodeFromSinglyLinkedList(self):
    if self.length ==0:
        print("List is empty")
    else:
        currentNode =self.head
        previousNode =self.head
        while currentNode.next!=None:
            previousNode =previousNode.next
            currentNode =currentNode.next
        previousNode.next = None
        self.length -=1