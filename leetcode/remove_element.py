# https://leetcode.com/problems/remove-element/

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if nums is None: return 0
        j = 0
        for i in range(len(nums)):
            n = nums[i]
            if n != val:
                nums[j] = n
                j += 1
        return j