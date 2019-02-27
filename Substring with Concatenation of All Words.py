'''
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
'''


class Solution:
    def delList(self, words, word):
        n = len(words)
        for i in range(n):
            if words[i] == word:
                return words[:i] + words[i + 1:], True
        return words, False

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        words_num = len(words)
        words_len = len(words[0])
        ans = []
        i = 0
        n = len(s)
        while (i < n and i + words_len * words_num <= n):
            temp = words
            j = i
            state = True
            while (temp != [] and state):
                temp, state = self.delList(temp, s[j:j + words_len])
                j = j + words_len
            if temp == [] and state:
                ans.append(i)
            i = i + 1
        return ans


test = Solution()
print(test.findSubstring("barfoothefoobarman",
["foo","bar"]))