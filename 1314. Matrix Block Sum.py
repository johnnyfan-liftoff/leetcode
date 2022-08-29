


def matrixBlockSum(mat, k):
  row, col = len(mat), len(mat[0])
  res = [[0]* col for _ in range(row)]
  for i in range(row):
    for j in range(col):
      t = i - k
      l = j - k

      b = i + k
      r = j + k

      t = t if t >= 0 else 0
      l = l if l >= 0 else 0
      b = b if b <= row - 1 else row - 1
      r = r if r <= col - 1 else col - 1

      res[i][j] = count(mat, t, b, l , r)

  return res

def count(mat, t, b, l, r):
  sum = 0
  for i in range(t, b + 1):
    for j in range(l, r + 1):
      sum = sum + mat[i][j]
  return sum


###############
def matrixBlockSum2(mat, k):
  row, col = len(mat), len(mat[0])
  res = [[0]* col for _ in range(row)]
  for i in range(row):
    for j in range(col):
      t = i - k if i - k >= 0 else 0
      l = j - k if j - k >= 0 else 0
      b = i + k if i + k <= row - 1 else row - 1
      r = j + k if j + k <= col - 1 else col - 1
      
      sum = 0
      for p in range(t, b + 1):
        for q in range(l, r + 1):
          sum = sum + mat[p][q]    
      res[i][j] = sum
  return res

###############
### DP 
def matrixBlockSum3(mat, k):
  row, col = len(mat), len(mat[0])
  res = [[0]* col for _ in range(row)]
  pre = [[0]* col for _ in range(row)]

  for i in range(row):
    for j in range(col):
      if i - 1 < 0 and j - 1 < 0:
        pre[i][j] = mat[i][j]
      elif i - 1 < 0:
        pre[i][j] = mat[i][j] + pre[i][j-1]
      elif j - 1 < 0:
        pre[i][j] = mat[i][j] + pre[i-1][j]
      else:
        pre[i][j] = mat[i][j] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]
  
  for i in range(row):
    for j in range(col):
      t = i - k - 1 if i - k - 1 >=0 else 0
      l = j - k - 1 if j - k - 1 >=0 else 0
      b = i + k if i + k <row else 0
      r = j + k if j + k <row else 0

      if i - k - 1 < 0 and j - k - 1 < 0:
        res[i][j] = pre[i+k][j+k]
      elif i - k - 1 < 0:
        res[i][j] = pre[b][r] - pre[b][r-k-1]
      elif l < 0:
        res[i][j] = pre[b][r] - pre[t][l]
      else:
        res[i][j] = pre[b][r] - pre[t][r] - pre[l][b] + pre[t][l]

     

      # res[i][j] = pre[b][r] - pre[t][r] - pre[b][l] + pre[t][l]

  return res




mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(matrixBlockSum3(mat, k))

8938

        # 1 2 3 4 4
        # 4 5 6 5 5
        # 7 8 9 6 6
        # 7 8 9 6 6
        # 7 8 9 6 6

        # [[1, 3, 6], 
        #  [5, 12, 21], 
        #  [12, 27, 45]]

        # [12,21,16],
        # [27,45,33],
        # [24,39,28]]