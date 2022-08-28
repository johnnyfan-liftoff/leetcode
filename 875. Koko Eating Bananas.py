import math
def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    k = 0
    maxp = max(piles)
    res = maxp   
    l, r = 0, res
    while l <= r:
        total = 0
        k = (r - l) // 2 + l
        for i in piles:
            total = total + i // k
            if i % k != 0:
                total += 1
        if total <= h:
            r = k - 1
        else:
            l = k + 1
    return l

piles = [3,6,7,11]
h = 8

print(minEatingSpeed(piles, h))