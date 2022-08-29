

from curses.ascii import isdigit

def calculate(s: str) -> int:
        if not s: return 0 
        symbols, symbol = ["+", "-", "*", "/"], "+"
        cur, stack = 0, []
        for index in range(len(s)):
            char = s[index]
            if char.isdigit():
                cur = cur * 10 + int(char)
                
            if char in symbols or index == len(s) - 1:
                if symbol == "+":
                    stack.append(cur)
                elif symbol == "-":
                    stack.append(-cur)
                elif symbol == "*":
                    stack[-1] = stack[-1] * cur    
                elif symbol == "/":
                    print(int(-3/2))
                    stack[-1] = int(stack[-1]/cur)
                cur = 0 
                symbol = char 
                
        return sum(stack)

# print(calculate("2+4+3*8*2"))

def calc(item):
  op1 = 0
  op2 = 1
  op = ""
  p = 0
  for i in item:
    if i == "+":
      print (op1)
      print (op2)
      op2 = op1 + p
      op1 = op2
      op = i
    elif i == "*":
      if op == "*":
        op2 = p

      op2 = p * op2
      print(op2)
      op = i
    elif i.isdigit():
      p = p * 10 + int(i)


  return op1 + op2 * p

print(calc("2+4+3*8*2"))
