# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBalancedRec(root):
            """
            :type root: TreeNode
            :rtype: (bool, int)
            """
            if root is None: 
                return (True, 0)

            h = 0
            h_diff = 0

            if root.left is not None:
                left_bal, left_h = isBalancedRec(root.left)
                if not left_bal:
                    return (False, 0)
                h = left_h
                h_diff += left_h
                
            if root.right is not None:
                right_bal, right_h = isBalancedRec(root.right)
                if not right_bal:
                    return (False, 0)
                h = max(h, right_h)
                h_diff -= right_h
                
            return (abs(h_diff) <= 1, h + 1)
            
        bal, _ = isBalancedRec(root)
        return bal
        

