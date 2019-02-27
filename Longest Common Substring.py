class Solution:
    def __init__(self):
        self.s1 = 'OldSite:GeeksforGeeks.org'
        self.s2 = 'NewSite:GeeksQuiz.com'

    def longest_common_string(self):
        m = len(self.s1)
        n = len(self.s2)
        suffix = [[0 for k in range(n+1)] for l in range(m+1)]
        result = 0

        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    suffix[i][j] = 0
                elif self.s1[i - 1] == self.s2[j - 1]:
                    suffix[i][j] = suffix[i-1][j-1] + 1
                    result = max(result, suffix[i][j])
                else:
                    suffix[i][j] = 0
        return result

test = Solution()
print(test.longest_common_string())

