def fio(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fio(n-1) + fio(n-2)
    
num = int(input().strip())
print (fio(num))