# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareSymetricTrees(tree1, tree2):
            if tree1 is None and tree2 is None: 
                return True
            if ((tree1 is None and tree2 is not None) or 
                (tree2 is None and tree1 is not None)):
                return False
            return (
                tree1.val == tree2.val and
                compareSymetricTrees(tree1.left, tree2.right) and 
                compareSymetricTrees(tree1.right, tree2.left))
                
        return compareSymetricTrees(root.left, root.right) if root is not None else True