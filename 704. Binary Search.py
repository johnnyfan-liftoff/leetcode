def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        t = (r - l) // 2 + l
        if target == nums[t]:
            return t
        elif target > nums[t]:
            l = t + 1
        else:
            r = t - 1
    return -1



nums = [-1,0,3,5,9,12]
target = 5

print (search(nums, target))