# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        start = ListNode(None)
        start.next = head
        prev = start
        while head is not None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return start.next