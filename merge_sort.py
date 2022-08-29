
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  size = len(arr)
  left = arr[:size//2]
  right = arr[size//2:]
  left = merge_sort(left)
  right = merge_sort(right)

  i, j, k = (0, 0, 0)
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1

  if i == len(left):
    while j < len(right):
      arr[k] = right[j]
      k += 1
      j += 1
  else:
      arr[k] = left[i]
      k += 1
      i += 1

  return arr
  
a = [3, 5, 6, 9, 39, 2]
print(merge_sort(a))






arr = [5, 8, 1, 3, 7, 9, 2]

print(merge_sort(arr))
