def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l <= r:
      if target == nums[l]:
        return l
      elif target == nums[r]:
        return r
      m = (l + r) // 2
      if target == nums[m]:
        return m
      elif target < nums[l]:
        l = m + 1
      elif nums[m] > target:
        r = m - 1
      else:
        l = m + 1
    return -1



nums = [5,1,2,3,4]
target = 1
print(search(nums, target))