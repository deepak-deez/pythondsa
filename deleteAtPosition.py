def deleteAtPosition(self,pos):
    count =0
    currentnode =self.head
    previousnode =self.head
    if pos>self.length or pos <0:
        print("The position does not exist. please enter a valid position")
    else:
        while currentnode!=None and count<pos:
            count+=1
            if count ==pos:
                previousnode.next =currentnode.next
                self.length-=1
                return
            else:
                previousnode =currentnode
                currentnode =currentnode.next
