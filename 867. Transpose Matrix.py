def transpose(matrix):
  """
  :type matrix: List[List[int]]
  :rtype: List[List[int]]
  """

  row, col = len(matrix), len(matrix[0])

  for y in range(1, col):
    for x in range(0, row-1):
      if 0 <= x < row and 0 <= y <col and 0 <= y < row and 0 <= x <col :
        matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

matrix = [[1,2,3,4],
          [4,5,6,7]]

transpose(matrix)
print (matrix)