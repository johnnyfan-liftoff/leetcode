def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    product = 1
    for i in nums:
      product *= i

    res = []
    for index, i in enumerate(nums):
      newprod = 1
      if i == 0:
        for index2, j in enumerate(nums):
          if index != index2:
            newprod *= j
        res.append(newprod)
      else:
        res.append(product//i)

    return res


nums = [1,2,3,4]
print(productExceptSelf(nums))