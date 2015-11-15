# https://leetcode.com/problems/search-insert-position/

    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        def binary_search(nums, target, i, j):
            # base case -> return idx
            if j - i == 1:
                return i if target <= nums[i] else j
            # find k (mid)
            k = i + (j - i) / 2
            if target >= nums[k]:
                return binary_search(nums, target, k, j)
            else: 
                return binary_search(nums, target, i, k)
               
        return binary_search(nums, target, 0, len(nums))