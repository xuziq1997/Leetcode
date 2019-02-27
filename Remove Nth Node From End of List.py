'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        temp2 = dummy
        count = 0
        if head.next == None:
            return None

        while count <= n:
            temp = temp.next
            count += 1
        while temp:
            temp = temp.next
            temp2 = temp2.next

        temp2.next = temp2.next.next
        temp2 = None
        return dummy.next