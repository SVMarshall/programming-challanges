# https://leetcode.com/problems/house-robber/

class Solution(object):
    solutions = {}
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return nums[0]

        nums_str = str(nums)
        if nums_str in self.solutions:
            return self.solutions[nums_str]

        # picking (or not) the current element
        res = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        self.solutions[nums_str] = res
        return res