#takes a linked list as a input
def length(self):
    current = self.head
    count= 0
    while current!=None:
        count = count+1
        current = current.next
    return count
