# https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur_list = [0, 1, 0]
        for _ in range(rowIndex):
           new_list = [cur_list[i] + cur_list[i + 1] for i in range(len(cur_list) - 1)]
           cur_list = [0] + new_list + [0]
        return cur_list[1:-1]
