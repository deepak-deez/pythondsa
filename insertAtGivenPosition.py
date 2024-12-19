from linkedList import Node
import insertAtEnd
import insertAtBeginning

def insertAtGivenPosition(self,pos,data):
    if pos>self.length or pos<0:
        return None
    else:
        if pos ==self.length:
            self.insertAtEnd(data)
        elif pos ==0:
            self.insertAtBeginning(data)
        else:
            newNode =Node()
            newNode.data =data
            count = 1
            current =self.head
            while count < pos-1:
                count+=1
                current =current.next
            newNode.next =current.next
            current.next =newNode
            self.length+=1