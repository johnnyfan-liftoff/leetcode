from collections import deque

# You are given a string representing a mathematical operation
# that is expressed using postfix notation. In postfix notation
# operations are performed in the order 
# in which they are written (left to right).
# E.g:
#   "3 + 2" would be "3 2 +" in postfix notation
#   "(8 - 2) * 3" would be "8 2 - 3 *" in postfix notation

def eval(expression: str) -> int:
    # implement this
    q = deque()

    ops = "+-*/"

    items = expression.strip().split(" ")
    result = 0
    for i in items:
      if i in ops:
        a = q.pop()
        b = q.pop()
        if i == "+":
          result = a + b
        elif i == "-":
          result = b - a
        elif i == "*":
          result = a * b
        elif i == "/":
          result = b / a
        q.append(result)
      else:
        q.append(int(i))
    return result


if __name__ == "__main__":
    assert eval("8 2 *") == 8 * 2
    assert eval("7 2 - 2 *") == (7 - 2) * 2;
    assert eval("35 7 / 5 -") == (35 / 7) - 5
    assert eval("3 2 8 + 9 - *") == (2 + 8 - 9) * 3
    print (eval("3 2 8 + 9 - *"))
    print ("done")

