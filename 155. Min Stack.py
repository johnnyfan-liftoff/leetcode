import heapq


class MinStack(object):

    def __init__(self):
      self.st = []
      self.min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st.append(val)
        self.min.append(val)
        heapq.heapify(self.min)
        
    def pop(self):
        """
        :rtype: None
        """
        return self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()