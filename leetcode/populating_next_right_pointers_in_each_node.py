# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        to_visit = []
        if root is not None: 
            to_visit.append(root)
        while to_visit:
            next_level = []
            # 1. travel through all queued nodes and set next
            next_ref = None
            while to_visit:
                current = to_visit.pop(0)
                current.next = next_ref
                next_ref = current
                if current.right is not None: 
                    next_level.append(current.right)
                if current.left is not None: 
                    next_level.append(current.left)
            # 2. queue next tree level 
            to_visit = list(next_level)
