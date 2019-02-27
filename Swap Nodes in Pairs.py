# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = head
        while (s != None and s.next != None):
            j = s.val
            s.val = s.next.val
            s.next.val = j
            s = s.next.next
        return head