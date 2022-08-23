from argparse import ArgumentError


def threeSum(nums):
    arr = sorted(nums)
    res = []
    for i, a in enumerate(arr):
        if i > 0 and a == arr[i - 1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            if arr[l] + arr[r] + a == 0:            
                res.append(sorted([arr[l], arr[r], a]))
                l += 1
                while arr[l] == arr[l-1] and l < r:
                    l += 1
            elif arr[l] + arr[r] + a > 0:
                r -= 1
            elif arr[l] + arr[r] + a < 0:
                l += 1
    return res


nums = [-1,0,1,2,-1,-4]
print (threeSum(nums))