# https://leetcode.com/problems/summary-ranges/

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        prev = None
        rank_start = None
        ranks = []
        for num in nums: 
            if prev is None: 
                # new set
                rank_start = num
            elif num != prev + 1: 
                # save set & new set
                ranks.append("{0}->{1}".format(rank_start, prev) if rank_start != prev
                			 else "{0}".format(rank_start))
                rank_start = num
            prev = num
        if prev is not None: 
            ranks.append("{0}->{1}".format(rank_start, prev) if rank_start != prev
            			 else "{0}".format(rank_start))
        return ranks