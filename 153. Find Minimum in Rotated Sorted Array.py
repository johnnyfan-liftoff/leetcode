def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    res = nums[0]
    while l <= r:
      if nums[l] < nums[r]:
        res = min(res, nums[l])
        break
      m = (l + r) // 2
      res = min(res, nums[m])
      if nums[l] <= nums[m]:
        l = m + 1
      else:
        r = m - 1
    return res


# nums = [3,4,5,6,7,8,1,2]
nums = [7,8,1,2,3,4,5,6]
# nums = [4,5,6,7,0,1,2]
print(findMin(nums))