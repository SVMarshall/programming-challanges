# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find_nodes_dfs(root, p, q):
            # recursively find all nodes in list
            if root is None: 
                return False

            to_be_found = 2  # len([p, q])
            found = 0

            # find on left
            if root.left is not None and p.val < root.val:
                found_left,  anc_left  = find_nodes_dfs(root.left, p, q)
                found += found_left
                if found_left == to_be_found:
                    return (found_left, anc_left)

            # find on right
            if root.right is not None and q.val > root.val:
                found_right, anc_right = find_nodes_dfs(root.right, p, q)
                found += found_right
                if found_right == to_be_found:
                    return (found_right, anc_right)

            # maybe with current node
            if root in [p, q]:
                found += 1

            return (found, root)

        lo, hi = (p, q) if p.val < q.val else (q, p)
        _, comm_anc = find_nodes_dfs(root, lo, hi)
        return comm_anc