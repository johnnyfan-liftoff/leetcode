


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row, col = len(matrix), len(matrix[0])
    x, y = 0, row - 1

    while x < col and y >= 0:
      if target == matrix[y][x]:
        return True
      elif target > matrix[y][x]:
        x += 1
      elif target < matrix[y][x]:
        y -= 1

    return False


matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]

target = 21
print (searchMatrix(matrix, target))