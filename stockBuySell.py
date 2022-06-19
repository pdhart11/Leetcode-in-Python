class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        num = prices[0]
        i = 0
        for i in range(len(prices) - 1):
            if prices[i] < num:
                num = prices[i]
                i+=1
            else:
                i+=1
            if prices[i] > num:
                profit.append(prices[i] - num)
                i+=1
        return max(profit, default = 0)
