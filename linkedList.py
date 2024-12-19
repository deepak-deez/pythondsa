#node of a singly LinkedList
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next =next
    def setData(self,data):
        self.data =data
    def getData(self,data):
        return self.data
    def setNext(self, next):
        self.next =next
    def getNext(self, next):
        return self.next
    def hasNext(self):
        return self.next!=None
    
#class for defining a linkedList    
class LinkedList(object):
    def __init__(self ,node=None):
        self.length =0
        self.head = node

