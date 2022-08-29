
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    d = {}
    for i in nums:
        if i in d:
            return True
        else:
            d[i] = 0
    return False


nums = [1,2,3,4]
print(containsDuplicate(nums))
