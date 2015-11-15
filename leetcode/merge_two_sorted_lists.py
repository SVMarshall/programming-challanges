# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = last = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val: 
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        if l1 is not None: 
            last.next = l1
        if l2 is not None: 
            last.next = l2
        return head.next