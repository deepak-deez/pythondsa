def deleteFromBeginning(self):
    if self.length ==0:
        print("list is empty")
    else:
        self.head =self.head.next
        self.length -=1
        