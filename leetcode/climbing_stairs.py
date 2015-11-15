# https://leetcode.com/problems/climbing-stairs/

class Solution:
    results = {}
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 2:
            return n
        res = self.results.get(n)
        if res is None:
            a = self.climbStairs(n - 1)
            b = self.climbStairs(n - 2)
            res = a + b
            self.results[n] = res
        return res