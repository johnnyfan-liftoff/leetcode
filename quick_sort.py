import random
import sys

def quick_sort(arr, left, right):
    if right - left <= 1:
      return arr
    if left < right:
        pi = partition2(arr, left, right)
        quick_sort(arr, left, pi - 1)
        print (arr[pi: right]) 
        quick_sort(arr, pi + 1, right)
        print (arr[pi: right]) 
       
    

def partition(arr, start, end):
    pivot = start
    i = start
    j = end
    
    while i <= j:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while i <= j and arr[j] > arr[pivot]:
            j -= 1
        if i <= j:
            arr[j], arr[i] = arr[i], arr[j]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

def partition2(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high



# Quick sort in Python

# function to find the partition position
def part(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [5, 8, 1, 3, 7, 9, 2]
quick_sort(data, 0, len(data) - 1)
print(data)

# arr = [4, 2, 8, 3, 1, 5, 7, 11, 6]
# arr = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
# arr= [5, 8, 1, 3, 7, 9, 2]

# quick_sort(arr, 0, len(arr)-1)

