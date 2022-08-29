class Queue:
    def __init__(self):
        self._q = []
    
    def dequeue(self):
        del self._q[0]
    
    def enqueue(self, data):
        self._q.append(data)

    def head(self):
        return self._q[0]
        
    def print(self):
        s = ""
        for i in self._q:
            s += " " + str(i) 
        return s

num = int(input().strip())

q = Queue()
for i in range(num):
  cmd = input().strip().split(' ')
  if cmd[0].strip() == '1':
    q.enqueue(int(cmd[1]))
  elif cmd[0] == '2':
    q.dequeue()
  elif cmd[0] == '3':
    print (q.head())
