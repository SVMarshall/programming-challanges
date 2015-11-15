# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1 if nums else 0