
def rotate(matrix):
  n = len(matrix)
  t, b, l, r = 0, n - 1, 0, n - 1

  while l <= r:
    for i in range(r - l):
      # rotate
      tmp = matrix[t][l+i]
      #(3, 0) -> (0, 0)
      matrix[t][l+i] = matrix[b-i][l]
      
      #(3, 3) -> (3, 0)
      matrix[b-i][l] = matrix[b][r-i]
      
      #(0, 3) -> (3, 3)
      matrix[b][r-i] = matrix[t+i][r]

      matrix[t+i][r] = tmp
      
    t += 1
    b -= 1
    l += 1
    r -= 1

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]

print (rotate(matrix))
print (matrix)