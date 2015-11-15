# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None: return head
        current = head
        while current.next is not None: 
            if current.val == current.next.val:
                current.next = current.next.next
            else: 
                current = current.next
        return head