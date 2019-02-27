'''
    Given a string, find the length of the longest substring without repeating characters.
'''


class Solution:
    def __init__(self):
        self.s = 'abcabcbb'

    def lengthOfLongestSubstring(self):
        """
        :type s: str
        :rtype: int
        """
        s = self.s
        s_len = len(s)
        if s_len == 0:
            return 0
        longest_length = 1
        for start in range(s_len):
            current_index = start
            current_len = 1
            given_letter = s[current_index]
            if current_index == s_len - 1:
                pass
            else:
                while (current_index + 1 <= s_len - 1 and s[current_index + 1] not in given_letter):
                    current_index += 1
                    given_letter += s[current_index]
                    current_len += 1
            if current_len > longest_length:
                longest_length = current_len
        return longest_length

test = Solution()
print(test.lengthOfLongestSubstring())
