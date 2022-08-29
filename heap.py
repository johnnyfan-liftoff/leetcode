


def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and arr[i] > arr[l]:
    largest = l

  if r < n and arr[largest] > arr[r]:    
    largest = r

  if largest != i: 
    arr[largest], arr[i] = arr[i], arr[largest] 
    heapify(arr, n, largest)


def heapify1(arr, n, i): 
 largest = i # Initialize largest as root 
 l = 2 * i + 1  # left = 2*i + 1 
 r = 2 * i + 2  # right = 2*i + 2 
  
 # See if left child of root exists and is 
 # greater than root 
 if l < n and arr[i] < arr[l]: 
  largest = l 
  
 # See if right child of root exists and is 
 # greater than root 
 if r < n and arr[largest] < arr[r]: 
  largest = r 
  
 # Change root, if needed 
 if largest != i: 
  arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
  # Heapify the root. 
  heapify(arr, n, largest) 

# arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
# # arr = [1, 12, 9, 5, 6, 10]

# l = len(arr)
# for i in range(l//2-1, -1, -1):
#   heapify(arr, l, i)

# for i in range(l-1, 0, -1): 
#   print (arr[0])
#   arr[i], arr[0] = arr[0], arr[i] # swap 
#   heapify(arr, i, 0) 

# print(arr)


arr =[]
n = int(input().strip())

for _ in range(n):
    items = input().split()
    if len(items) == 1 and int(items[0]) == 3:
        print(arr[0])
    else:
        cmd, value = items
        if int(cmd) == 1:
            arr.append(int(value))
            heapify(arr, len(arr), len(arr)//2 -1)
        elif int(cmd) == 2:
            k = 0
            for j in range(len(arr)):
              if arr[j] == int(value):
                k = j 
                break
            num = len(arr) - 1
            arr[0], arr[k] = arr[k], arr[0] # swap     
            arr[0], arr[num] = arr[num], arr[0]
            del arr[num]
            heapify(arr, len(arr), len(arr)//2 -1) 
            