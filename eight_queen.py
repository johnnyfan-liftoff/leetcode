from collections import deque

def eight():
  m = [[0 for i in range(8)] for j in range(8)]

  q = deque()

  for i in range(8):
    for j in range(8):
      m [i, j] = 1
      q.append((i, j))


  print (m)








print(eight())