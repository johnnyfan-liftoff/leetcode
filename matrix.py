


def matrix(arr):
  directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1, 1], [1, -1]]

  for d in directions:
    nx, ny = 0, 0
    print(arr[nx][ny], end="")
    for _ in range (2*len(arr) -1):
      (nx, ny) = nx + d[0], ny + d[1]
      if 0 <= nx < len(arr) and 0 <= ny < len(arr):
        print(arr[nx][ny], end="")
    print("")

arr = [[3,2,4,5],
       [4,1,7,9],
       [3,6,1,5],
       [4,8,0,1]]

matrix(arr)