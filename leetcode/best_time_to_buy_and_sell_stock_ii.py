# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if (len(prices) > 0):
            last_price = last_min = prices[0]
            for price in prices[1:]:
                if price >= last_price: 
                    profit = profit + price - last_price
                last_price = price
        return profit