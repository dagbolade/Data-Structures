class Stack:
  def __init__(self):
        self.internalArray = []
        self.size = 0
      
  def push(self, item):
      self.internalArray.append(item)
      self.size += 1
      
  def pop(self):
    
    if len(self.internalArray) == 0:
          print("Stack is empty")
    else:      
      del self.internalArray[-1] 
      return self.internalArray[-1] 
    
   
       
  def __str__(self):
        return self.internalArray.__str__()
        
stack1 = Stack()
print(stack1)
stack1.push('Linux')
stack1.push("Windows")
stack1.push("Mac Os X")          
 