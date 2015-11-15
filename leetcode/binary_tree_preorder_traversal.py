# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        to_visit = []
        if root is not None: 
            to_visit.append(root)
        to_print = []
        while to_visit:
            current = to_visit.pop()
            if current.right is not None: 
                to_visit.append(current.right)
            if current.left is not None: 
                to_visit.append(current.left)
            to_print.append(current.val)
        return to_print