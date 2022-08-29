class MaxStack1():
  def __init__(self):
    self.st = []
    self.max = []

  def push(self, x):
    # -- Push element x onto stack.
    if len(self.max) == 0:
      self.max.append(x)
    else:
      self.max.append(max(x, self.max[-1]))
    self.st.append(x)

  def pop(self):
    # -- Remove the element on top of the stack and return it.
    self.max.pop()
    return self.st.pop()

  def top(self):
    # -- Get the element on the top.
    return self.st[-1]

  def peekMax(self):
    #  -- Retrieve the maximum element in the stack.
    return self.max[-1]

  def popMax(self):
    #
    tmp = []
    max  = self.max[-1]
    while self.pop() != max:
      self.max.pop()
      tmp.append(self.pop())

    while tmp:
      t = tmp.pop()
      self.st.append(t)
      if len(self.max) == 0:
        self.max.append(t)
      else:
        self.max.append(max(t, self.max[-1]))


# practice
class MaxStack():
  def __init__(self):
    self.st = []
    self.max = []

  def push(self, x):
    if len(self.st) == 0:
      self.max.append(x)
    else:
      self.max.append(max(x, self.max[-1]))
    self.st.append(x)

  def pop(self):
    self.max.pop()
    return self.st.pop()
    
  def top(self):
    return self.st[-1]

  def peekMax(self):
    return self.max[-1]
    
  def popMax(self):
    m = self.max[-1]
    tmp = []
    
    t = self.st.pop()
    self.max.pop()
    while m != t:
      tmp.append(t)
      t = self.st.pop()
      self.max.pop()

    for i in tmp:
      self.push(i)

stack = MaxStack()
stack.push(5) 
stack.push(1)
stack.push(5)
print(stack.top()) #-> 5
print(stack.popMax()) #-> 5
print(stack.top()) #-> 1
print(stack.peekMax()) #-> 5
print(stack.pop()) #-> 1
print(stack.top()) #-> 5