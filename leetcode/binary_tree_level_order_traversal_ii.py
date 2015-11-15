# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def mergeLists(l1, l2):
            len_l1, len_l2 = len(l1), len(l2)
            if len(l1) >= len(l2):
                lr = list(l1)
                while len_l2 > 0:
                    lr[len_l1 - 1] = l1[len_l1 - 1] + l2[len_l2 - 1]
                    len_l1 -= 1
                    len_l2 -= 1
            else:
                lr = list(l2)
                while len_l1 > 0:
                    lr[len_l2 - 1] = l1[len_l1 - 1] + l2[len_l2 - 1]
                    len_l1 -= 1
                    len_l2 -= 1
            return lr
        
        if root is None: 
            return []
        return mergeLists(self.levelOrderBottom(root.left), self.levelOrderBottom(root.right)) + [[root.val]]
