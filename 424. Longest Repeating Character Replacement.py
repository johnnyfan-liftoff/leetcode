def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    maxP = 0
    h = []
    l, r = 0, 1
    while r < len(s):
        if s[r] != s[l]:
            if len(h) < k:
                h.append(r)
                maxP = max(maxP, r - l + 1)
            else:
                h = []
                l = r
                while s[r] == s[l-1] and l-1 >= 0 :
                    l -= 1
                maxP = max(maxP, r - l + 1)
        else:
            maxP = max(maxP, r - l + 1)
        r += 1
    return maxP

s = "AABABBA"
k = 1
# s = "ABAB"
# k = 2
# s = "AAAA"
# k = 2
s = "ABBB"
k = 2
# s = "AABA"
# k = 0
print(characterReplacement(s, k))