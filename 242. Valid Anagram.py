def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = {}
    for i in s:
      if i in d:
        d[i] = d[i] + 1
      else:
        d[i] = 1

    for i in t:
      if i in d:
        if d[i] == 1:
          del d[i]
        else:
          d[i] = d[i] - 1
      else:
        return False
    
    if d: 
      return False
    else:
      return True


s = "anagram"
t = "nagaram"

print(isAnagram(s, t))