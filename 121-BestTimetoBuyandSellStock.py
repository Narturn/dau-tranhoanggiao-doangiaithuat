class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        sell = prices[0]

        for i in prices:
            if i < sell:
                sell = i
            else:
                max_profit = max(max_profit, i - sell)
            
        return max_profit