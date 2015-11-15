# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head: return head
        cur = head
        pre = None
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre