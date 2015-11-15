# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            if carry == 1:
                carry     = (digits[i] + 1) / 10
                digits[i] = (digits[i] + 1) % 10
            else: 
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits