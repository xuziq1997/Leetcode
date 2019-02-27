'''
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.
'''


class Solution:
    def __init__(self):
        self.test = "ab"

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = self.test
        maxLength = 1

        start = 0
        length = len(s)

        low = 0
        high = 0
        for i in range(1, length):
            # Find the longest even length palindrome with center
            # points as i-1 and i.
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            # Find the longest odd length palindrome with center
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        print("Longest palindrome substring is:" + s[start:start + maxLength]),

        return maxLength

test = Solution()
print(test.longestPalindrome())




