# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        write_p = 0
        read_p = 0
        while read_p < len(nums):
            if nums[read_p] != 0: 
                num = nums[read_p]
                nums[read_p] = 0
                nums[write_p] = num
                write_p += 1
            read_p += 1