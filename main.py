class Node:

 def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None
#make sure your def is well indented
#just one space from yourclass
 def link(self, otherNode):#otherNode will link to the data
      self.next = otherNode #this is for the forward link
      otherNode.prev = self #this is for the backward link

      
 def __str__(self):
  return self.data.__str__()

class Linkedlist:
  def __init__(self):

    self.first = None

    self.last = None

  def add(self, data):
    new_node = Node(data)
    new_node.next = self.first
    self.first = new_node
    if self.first is None:
            self.first = new_node
            return




n1 = Node("Fred")
n2 = Node("Tom")
n3 = Node("David")
print(n1)
print(n2)   
print(n3)

#link nodes together
n1.link(n2)
n2.link(n3)

#print the next and previous
print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)
print(n3.prev)
print(n3.next)

