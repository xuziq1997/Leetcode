# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def remainKElement(self, head, k):
        i = 0
        s = head
        while (i < k):
            if s != None:
                s = s.next
                i = i + 1
            else:
                return False
        return True

    def swapKElement(self, head, k):
        i = 0
        s = head
        array = []
        while (i < k):
            array.append(s.val)
            s = s.next
            i = i + 1
        s = head
        j = 0
        while (j < k):
            s.val = array[k - j - 1]
            s = s.next
            j = j + 1
        return s

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        s = head
        while s != None and self.remainKElement(s, k):
            s = self.swapKElement(s, k)
        return head