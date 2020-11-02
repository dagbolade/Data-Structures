

class Stack:
  def __init__(self):
        self.internalArray = []
        self.size = 0

  def push(self, item):
      self.internalArray.append(item)
      self.size += 1
      
  def pop(self):
    del self.internalArray[-1] 
    return self.internalArray[-1] 
          
stack1 = Stack()
print(stack1.internalArray)
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1.internalArray)  
  
popped1 = stack1.pop()
print(popped1)
popped2 = stack1.pop()
print(popped2)    
