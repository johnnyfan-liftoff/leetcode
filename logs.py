def processLogs(logs, threshold):
  # Write your code here
  d = {}
  for i in logs:
    source,  dest, tran = i.strip().split(" ")
    if source == dest:
      if not source in d:
        d[source] = 1
      else:
        d[source] = d[source] + 1
    else:
      if not source in d:
        d[source] = 1
      else:
        d[source] = d[source] + 1

      if not dest in d:
        d[dest] = 1
      else:
        d[dest] = d[dest] + 1

  tr = [(k, v) for k, v in sorted(d.items(), key=lambda item: item[1])]

  res = []
  for k, v in tr:
    if v >= threshold:
      res.append(int(k))
  
  res.sort()
  res = [str(i) for i in res]
  return res



logs = ["88 99 200", "88 99 300", "99 32 100", " 12 12 15"]
threshold = 2

print(processLogs(logs, threshold))