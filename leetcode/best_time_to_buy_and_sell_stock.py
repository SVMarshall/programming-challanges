# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit = 0
        if (len(prices) > 0):
            curr_min = prices[0]
            for price in prices[1:]:
                curr_min = min(curr_min, price) 
                max_profit = max(max_profit, price - curr_min)
        return max_profit