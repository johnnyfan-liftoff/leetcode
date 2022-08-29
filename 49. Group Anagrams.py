def groupAnagrams(strs):
  d = {}

  for i in strs:
    t = "".join(sorted(i))
    if t in d:
      d[t].append(i)
    else:
      d[t] = []
      d[t].append(i)
  
  res = []
  for k,v in d.items():
    res.append(v)

  return res






strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))