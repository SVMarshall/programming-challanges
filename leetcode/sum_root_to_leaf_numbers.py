# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        def sumNumbers_rec(root):
            if not root: 
                return []
            if not root.left and not root.right:
                return [[root.val]]
            cur_nums = []
            if root.left:
                l_l = sumNumbers_rec(root.left)
                cur_nums += [[root.val] + n for n in l_l]
            if root.right: 
                r_l = sumNumbers_rec(root.right)
                cur_nums += [[root.val] + n for n in r_l]
            return cur_nums
        
        return sum([int(''.join(map(str,num))) for num in sumNumbers_rec(root)])
