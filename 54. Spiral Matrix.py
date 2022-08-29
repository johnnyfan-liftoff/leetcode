
from doctest import master


def spiralOrder1(matrix):
  row_s, row_l, col_s, col_l = 0, len(matrix), 0, len(matrix[0])

  directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  limits = [[1, 0, 0, 0], [0, 0, 0, -1], [0, -1, 0, 0], [0, 0, 1, 0]]
  total = row_l * col_l
  x, y, dir  = 0, 0, 0

  res = []

  for i in range(total):
    res.append(matrix[x][y])
    nx, ny = x + directions[dir][0], y + directions[dir][1]
    if row_s <= nx < row_l and col_s <= ny < col_l:
      x, y = nx, ny
    else:
      x, y = x + directions[(dir + 1)%len(directions)][0], y + directions[(dir + 1)%len(directions)][1]
      row_s, row_l, col_s, col_l = row_s + limits[dir][0], row_l + limits[dir][1], col_s + limits[dir][2], col_l + limits[dir][3]
      dir = (dir + 1) % len(directions)

  return res

# practice

def spiralOrder(matrix):
  row, col = len(matrix), len(matrix[0])

  directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  limits = [[1, 0, 0, 0],[0, 0, 0, -1], [0, -1, 0, 0], [0, 0, 1, 0]]
  top, bottom, left, right = 0, row - 1, 0, col - 1
  x, y, d = 0, 0, 0
  res = []
  for i in range(row * col):
    res.append(matrix[x][y])
    nx = x + directions[d][0]
    ny = y + directions[d][1]
    if top <= nx <= bottom and left <= ny <= right:
      x, y = nx, ny
    else:
      d = (d + 1) % 4
      x, y = x + directions[d][0], y + directions[d][1]
      top, bottom, left, right = top + limits[d-1][0], bottom + limits[d-1][1], left + limits[d-1][2], right + limits[d-1][3]

  return res


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]]

print(spiralOrder(matrix))