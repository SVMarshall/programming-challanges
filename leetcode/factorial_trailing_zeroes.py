# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes = 0
        k = 5
        while k <= n: 
            zeroes += n / k
            k *= 5
        return zeroes