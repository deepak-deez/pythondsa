def deleteWithvalue(self,value):
    currentnode =self.head
    previousnode = self.head
    while currentnode.next!=None or currentnode.data!=value:
        if currentnode.data ==value:
            previousnode.next =currentnode.next
            self.length-=1
            return    
        else:
            previousnode =currentnode
            currentnode =currentnode.next
    print("The value provided is not present")
    