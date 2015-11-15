# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        def removeNthFromEnd_rec(head, n):
            if not head: 
                return 0
            my_pos = removeNthFromEnd_rec(head.next, n) + 1
            if my_pos - 1 == n:
                head.next = head.next.next
            return my_pos
        pre_head = ListNode(0)
        pre_head.next = head
        first_pos = removeNthFromEnd_rec(pre_head, n)
        return pre_head.next