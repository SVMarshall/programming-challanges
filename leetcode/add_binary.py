# https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # "a" to be the smallest string (or list)
        if len(a) > len(b): 
        	a, b = list(b), list(a)
        else: 
        	a, b = list(a), list(b)
        len_a, len_b = len(a), len(b)
        c = 0
        while len_a > 0: 
            s = int(b[len_b - 1]) + int(a[len_a - 1]) + c
            c = int(s / 2)
            b[len_b - 1] = str(s % 2)
            len_a -= 1
            len_b -= 1
        while len_b > 0:
            s = int(b[len_b - 1]) + c
            c = int(s / 2)
            b[len_b - 1] = str(s % 2)
            len_b -= 1
        if c == 1: 
            b.insert(0, "1")
        return "".join(b)