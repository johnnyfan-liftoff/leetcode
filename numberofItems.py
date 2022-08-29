def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    res = []
    d1 = []
    d2 = []
    count = 0
    i = 0

    size = len(s) - 1
    while s[size] == '*':
      size -= 1

    while s[i] == '*':
      i += 1
      d1.append(0)

    while i < size + 1:
      if s[i] == '*':
        count += 1
        d1.append(count)
      elif s[i] == '|':
        d1.append(count)
      i += 1

    d2 = [count - i for i in d1]

    for i in range(len(startIndices)):
        start, end = startIndices[0]-1, endIndices[0]-1
        while s[start] == '*':
          start += 1
        while s[end] == '*':
          end -= 1
        res.append(count - d1[start] - d2[end])
    return res         

s = "*|***|****|*****|**"
startIndices = [1, 1]
endIndices = [10, 11]
print (numberOfItems(s, startIndices, endIndices))