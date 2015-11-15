# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        while len(num_str) > 1: num_str = str(sum(map(int,num_str)))
        return int(num_str)