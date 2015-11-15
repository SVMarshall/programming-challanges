# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node is not None and node.next is not None:
            while node.next.next is not None:
                node.val = node.next.val
                node = node.next
            else:
                node.val = node.next.val
                node.next = None