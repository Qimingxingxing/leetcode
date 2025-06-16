class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        frontPro = [0] * n
        backPro = [0] * n
        maxPrice, minPrice = prices[-1], prices[0]
        for i in range(1, len(prices)):
            frontPro[i] = max(prices[i] - minPrice, frontPro[i - 1])
            minPrice = min(minPrice, prices[i])
        for i in range(len(prices) - 1)[::-1]:
            backPro[i] = max(maxPrice - prices[i], backPro[i + 1])
            maxPrice = max(maxPrice, prices[i])
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, frontPro[i] + backPro[i])
        return maxProfit
