


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    row, col = len(grid), len(grid[0])
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    island = 0
    q = []
    visited = set()

    for i in range(row):
      for j in range(col):
        if grid[i][j] == "0":
          continue
        if (i, j) in visited:
            continue
        else:
          q.append((i, j))
        while q:
          m, n = q.pop()
          if (m, n) in visited:
            continue
          else:
            visited.add((m, n))
            for d in directions:
              nm = m + d[0]
              nn = n + d[1]
              if not (0 <= nm < row and 0 <= nn< col):
                continue
              if (nm, nn) in visited:
                continue
              if grid[nm][nn] == "0":
                continue
              q.append((nm, nn))
        island += 1

    return island



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))