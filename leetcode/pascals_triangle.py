# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        cur_list = [0, 1, 0]
        for _ in range(numRows - 1):
           new_list = [cur_list[i] + cur_list[i + 1] for i in range(len(cur_list) - 1)]
           res.append(new_list)
           cur_list = [0] + new_list + [0]
        return res
