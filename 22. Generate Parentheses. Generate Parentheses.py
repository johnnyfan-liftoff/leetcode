def generateParenthesis(n):

    stack = []
    res = []

    def helper(left, right): 
        if n == left == right:
            res.append("".join(stack))
            return 
        if left < n:
            stack.append("(")
            helper(left + 1, right)
            stack.pop()
        if left > right:
            stack.append(")")
            helper(left, right + 1)
            stack.pop()

    helper(0, 0)
    return res


print(generateParenthesis(3))            




