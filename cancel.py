

s = "abbaca"
stack = []
for i in s:
    if len(stack) > 0 and i == stack[-1]:
      stack.pop()
    else:
      stack.append(i)
print( stack)