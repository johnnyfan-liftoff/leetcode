

def perm(l, result, size):
  if len(result) == size:
    print (result)
    return result
  for index, v in enumerate(l):
    result.append(l[index])
    # tmp.append(l[index])
    perm (l[:index] + l[index+1:], result, size)
    result.pop()
    # tmp.pop()


l = ['a', 'b', 'c', 'd']
tmp = l
result = []
perm(l, result, len(l))
print(result)