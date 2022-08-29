
def searchMatrix(matrix, target):
  """
  :type matrix: List[List[int]]
  :type target: int
  :rtype: bool
  """
  row, col = len(matrix), len(matrix[0])
  l, r = 0, row - 1
  while l <= r:
    if target == matrix[(r+l)//2][0]:
      return True
    elif target > matrix[(r+l)//2][0]:
      l = (r+l)//2 + 1
    elif target < matrix[(r+l)//2][0]:
      r = (r+l)//2 - 1

  r2 = r
  l, r = 0, col - 1
  while l <= r:
    if target == matrix[r2][(r+l)//2]:
      return True
    elif target > matrix[r2][(r+l)//2]:
      l = (r+l)//2 + 1
    elif target < matrix[r2][(r+l)//2]:
      r = (r+l)//2 - 1
  return False


def searchMatrix2(matrix, target):
  row, col = len(matrix), len(matrix[0])
  l, r = 0, row * col - 1
  while l <= r:
    mid = (r + l) // 2
    element = matrix[mid // col][mid % col]
    if element == target:
      return True
    elif target > element:
      l = mid + 1
    elif target < element:
      r = mid - 1
  return False

matrix = [[ 1, 3, 5, 7],
          [10,11,16,20],
          [23,30,34,60]]

matrix = [[1]]          
target = 1
print(searchMatrix2(matrix, target))

