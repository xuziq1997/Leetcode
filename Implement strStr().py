'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        n = len(haystack)
        while(i < n):
            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                i = i + 1
        return -1