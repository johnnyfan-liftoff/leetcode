
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    r = 0
    maxL = 0
    h = []

    while r < len(s):
        if s[r] not in h:
            h.append(s[r])
            maxL = max(maxL, len(h))
        else:
            while s[r] in h:
                h = h[1:]
            h.append(s[r])
        r += 1
    return maxL


s = "pwwkew"
print(lengthOfLongestSubstring(s))