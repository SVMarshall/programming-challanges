# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        visited = {}
        for i in range(len(nums)):
            if visited.get(nums[i]) is None:
                visited[nums[i]] = i
            elif i - visited[nums[i]] <= k:
                return True
            else: 
                visited[nums[i]] = i
        return False