
# Colorful Numbers
# February 22, 2015 by Sumit Jain
# Objective: Given a number, find out whether its colorful or not.

# Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

# Example:

# Given Number : 3245
# Output : Colorful

# Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# this number is a colorful number, since product of every digit of a sub-sequence are different.
# That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

# Given Number : 326

def color(item):
  s = str(item)
  t = [i for i in s]
  res = set()
  for i in range(1, len(t)+1):
    for j in range(len(t)-i+1):
      l = 1
      for k in t[j:j+i]:
        l *= int(k)
      if l in res:
        print (l)
        return "Not colorful"
      res.add(l)
  return "Colorful"

print(color(326))

