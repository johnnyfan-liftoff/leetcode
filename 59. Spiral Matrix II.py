

def generateMatrix(n):

  m = [[0] * n for _ in range(n)]

  directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  x, y = 0, 0
  d = 0
  step = n
  c = 0
  twice = 1
  for i in range(n * n):
    m[x][y] = i + 1
    c += 1
    if c == step:
      if twice == 1:
        step -= 1
        twice = 0
      else:
        twice += 1
      d = (d + 1) % 4
      c = 0
    x += directions[d%4][0]
    y += directions[d%4][1]

  return m


n = 5

print(generateMatrix(n))