
def toeplitz(matrix):
  row = len(matrix)
  col = len(matrix[0])
  for j in range(col):
    x, y = 0, j
    while 0 <= x < row and 0 <= y < col:
      if matrix[0][j] != matrix[x][y]:
        return False
      x, y = x + 1, y + 1
    
  for i in range(row):
    x, y = i, 0
    while 0 <= x < row and 0 <= y < col:
      if matrix[i][0] != matrix[x][y]:
        return False
      x, y = x + 1, y + 1
  
  return True


# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[11,74,0,93],
          [40,11,74,7]]
print(toeplitz(matrix))