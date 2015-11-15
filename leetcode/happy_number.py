# https://leetcode.com/problems/happy-number/

class Solution(object):
    results = {}
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n in self.results: return self.results[n]
        self.results[n] = False
        self.results[n] = self.isHappy(sum([int(i)**2 for i in str(n)]))
        return self.results[n]