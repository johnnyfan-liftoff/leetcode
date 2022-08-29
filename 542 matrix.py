

from collections import deque

def search(mat):
  level = 0
  for i in mat:
    for j in i:
      res = wrapper(mat, i, j, 0)


def wrapper(mat, x, y, level):
  if mat[x][y] == 0:
    return True
  l = 0
  q = deque()

  if x + 1 < len(mat):
    q.append((x+1, y, level))
  if y + 1 < len(mat[0]):
    q.append(x, y+1, level)
  if x - 1 >= 0:
    q.append(x-1, y, level)
  if y - 1 >= 0:
    q.append(x, y-1, level)


mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]

search(mat)