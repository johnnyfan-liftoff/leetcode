def twoSum(nums, target):
  d = {}
  for index, i in enumerate(nums):
    if i in d:
      return [index, d[i]]
    else:
      rem = target - i
      d[rem] = index 
  

nums = [3,2,4]
target = 6

print(twoSum(nums, target))