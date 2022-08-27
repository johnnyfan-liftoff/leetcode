def dailyTemperatures(temperatures):
    stack = []
    res = [0 for i in temperatures]

    for i, v in enumerate(temperatures):
        while stack and v > stack[-1][0]:
            val, ind = stack.pop()
            res[ind] = i - ind
        stack.append((v, i))
        
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))