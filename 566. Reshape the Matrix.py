
def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    
    row, col = len(mat), len(mat[0])

    if r * c != row * col:
      return mat

    res = [[0 for i in range(c)] for j in range(r)]
    x, y = 0, 0
    m, n = 0, 0
    for x in range(row):
      for y in range(col):
        res[m][n] = mat[x][y]
        if n + 1 < c:
          n += 1
        else:
          n = 0
          m += 1
    return res

mat = [[1,2],[3,4]]
r = 1
c = 4
print(matrixReshape(mat, r, c))