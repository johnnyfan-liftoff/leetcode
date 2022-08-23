def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    maxA = 0
    while l < r:
      maxA = max(maxA, min(height[l], height[r]) * (r - l))
      if height[l] > height[r]:
        r -= 1
      elif height[l] <= height[r]:
        l += 1
    return maxA
    
height = [1,8,6,2,5,4,8,3,7]
print (maxArea(height))