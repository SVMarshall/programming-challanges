# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # find len of A
        lenA = 0
        headA_tmp = headA
        while headA_tmp is not None:
            headA_tmp = headA_tmp.next
            lenA += 1
        # find len of B
        lenB = 0
        headB_tmp = headB
        while headB_tmp is not None:
            headB_tmp = headB_tmp.next
            lenB += 1
        # move heads to be equaly distant to the intersection (or not)
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        # now find the intersection
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA