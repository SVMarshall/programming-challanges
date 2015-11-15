# https://leetcode.com/problems/majority-element/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # O(n log n) soluction
        #counts = {}
        #for num in nums: 
        #    c = counts.get(num)
        #    c = 1 if c is None else c + 1
        #    counts[num] = c
        #    if c > len(nums)/2: return num
        #
        # O(n) solution
        candidate = None
        count = 0
        for num in nums: 
            if count == 0: 
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else: 
                count -= 1
        return candidate