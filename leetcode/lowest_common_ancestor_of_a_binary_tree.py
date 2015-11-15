# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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
        def find_nodes_dfs(root, nodes = []):
            # recursively find all nodes in list
            if root is None: 
                return False

            to_be_found = len(nodes)
            found = 0

            # all found on left
            if root.left is not None:
                found_left,  anc_left  = find_nodes_dfs(root.left, nodes)
                found += found_left
                if found_left == to_be_found: 
                    return (found_left, anc_left)

            # all found on right
            if root.right is not None:
                found_right, anc_right = find_nodes_dfs(root.right, nodes)
                found += found_right
                if found_right == to_be_found: 
                    return (found_right, anc_right)

            # maybe with current node
            if root in nodes: 
                found += 1

            return (found, root)

        _, comm_anc = find_nodes_dfs(root, [p, q])
        return comm_anc