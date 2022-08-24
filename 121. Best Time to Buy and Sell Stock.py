def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    l, r  = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return profit
    
prices = [7,1,5,3,6,4]
print(maxProfit(prices))