def deleteFromLinkedListWithNode(self,node):
    if self.length ==0:
        raise ValueError("List is empty")
    else:
        current = self.head
        previous = None
        found = False

        while not found:
            if current == node:
                found =True
            elif current == None:
                raise ValueError("Node not in Linked List")
            else:
                previous =current
                current =current.next
    if previous ==None:
        self.head = current.next
    else:
        previous.next = current.next
    self.length-=1
    