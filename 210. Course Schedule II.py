
def findOrder2(numCourses, prerequisites):

  preMap = {x:[] for x in range(numCourses)}
  [preMap[i[0]].append(i[1]) for i in prerequisites]

  visited, cycle = set(), set()
  result = []

  def dfs(i, visited, result):
    if i in cycle:
      return False
    
    if i in visited:
      return True
    
    cycle.add(i)
    for j in preMap[i]:
      if not dfs(j, visited, result): 
        return False
    
    cycle.remove(i)
    visited.add(i)
    result.append(i)
    return True

  for i in range(numCourses):
    if not dfs(i, visited, result):
      return []
  
  print (result)
  return result
  
  


# practice
def findOrder(numCourses, prerequisites):
  preMap = {i: [] for i in range(numCourses)}
  [preMap[i[0]].append(i[1]) for i in prerequisites]

  visited, cycle = set(), set()
  res = []

  def dfs(i):
    if i in cycle:
      return False
    if i in visited:
      return True
    
    cycle.add(i)
    for j in preMap[i]:
      if not dfs(j): 
        return False
    cycle.remove(i)
    visited.add(i)
    res.append(i)
    return True

  for i in range(numCourses):
    if not dfs(i):
      return []
  
  print (res)
  return res


# practice 3: 
# A → {B,C}
# B → {E}
# C → {D,E,F}
# D → {}
# F → {}
# G → {C}

def findOrder3(depends):
  totalSet = set()
  for i, v in depends.items():
    totalSet.add(i)
    for j in v:
      totalSet.add(j)
  
  for k in totalSet:
    if k not in depends:
      depends[k] = []
  
  print (totalSet)
  print (depends)

  visited, cycle = set(), set()
  res = []

  def dfs(p):
    if p in cycle:
      return False
    
    if p in visited:
      return True

    cycle.add(p)
    for j in depends[p]:
      if not dfs(j):
        return False

    visited.add(p)
    cycle.remove(p)
    res.append(p)
    return True

  for i in totalSet:
    if not dfs(i):
      return []
  
  return res
  

depends = {
  'A': ['B', 'C'],
  'B': ['E'],
  'C': ['D', 'E', 'F'],
  'D': [],
  'F': [],
  'G': ['C'],
}

print(findOrder3(depends))


numCourses = 5
# prerequisites = [[1,0],
#                  [2,0],
#                  [3,1],
#                  [3,2]]

prerequisites = [[0,1],
                 [0,2],
                 [1,3],
                 [3,4]]


findOrder(numCourses, prerequisites)