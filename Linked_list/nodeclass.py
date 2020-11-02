class Node:

 def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None
#make sure your def is well indented
#just one space from yourclass
 def link(self, otherNode):#otherNode will link to the data
      self.next = otherNode #this is for the forward link
      otherNode.prev = self#this is for the backward link

      
def __str__(self):
  return self.data.__str__()




n1 = Node("Fred")
n2 = Node("Tom")
print(n1)
print(n2)   

