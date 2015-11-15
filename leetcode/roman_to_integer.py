# https://leetcode.com/problems/roman-to-integer/

class Solution:
    # @param {string} s
    # @return {integer}
    sign_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    def romanToInt(self, s):
        from_val = 0
        res = 0
        for sign in reversed(s):
            val = self.sign_value[sign]
            if val >= from_val: 
                res += val
            else:
                res -= val
            from_val = val
        return res