

def topKFrequent(nums, k):
  d = {}
  for i in nums:
    if i in d:
      d[i] = d[i] + 1
    else: 
      d[i] = 1

  a = [(kk, v) for kk, v in sorted (d.items(), key=lambda item: item[1])]
  res = []
  for v in a[-k:]:
    res.append(v[0])
  return res



nums = [1,1,1,2,2,3]
k = 2


print(topKFrequent(nums, k))