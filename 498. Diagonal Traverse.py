def findDiagonalOrder(mat):
  """
  :type mat: List[List[int]]
  :rtype: List[int]
  """
  row, col = len(mat), len(mat[0])
  x, y = 0, 0
  direction = 1
  res = []
  for _ in range(row * col):
    if direction == 1:
      res.append(mat[x][y])
      x, y = x - 1, y + 1
      if x < 0 and y > col - 1:
        x += 1
        y -= 1
        x += 1
        direction *= -1
      elif x < 0:
        x = x + 1
        direction *= -1
      elif y > col - 1:
        x += 1
        y -= 1
        x += 1
        direction *= -1
    elif direction == -1:
      res.append(mat[x][y])
      x, y = x + 1, y - 1
      if x > row -1 and y < 0:
        x -= 1
        y += 1
        y += 1
        direction *= -1
      elif x > row - 1:
        x -= 1
        y += 1
        y += 1
        direction *= -1
      elif y < 0:
        y += 1
        direction *= -1
  return res  


# 需要考虑3种情况， x出界， y出界，x和y同时出界

mat = [[1,2,3],[4,5,6],[7,8,9]]  
mat = [[2,3]]    
print(findDiagonalOrder(mat))